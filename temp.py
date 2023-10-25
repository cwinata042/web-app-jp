import pandas as pd
import pyodide
import io
from js import document

table1 = document.getElementById('table1')
table2 = document.getElementById('table2')
table3 = document.getElementById('table3')
csv = None
df = None

async def get_file(e):
    files = e.target.files.to_py()
    for file in files:
      global df
      file_content = await file.text()
      df = pd.read_csv(io.StringIO(file_content))

      # Displays original table
      table1.innerHTML = ""
      table2.innerHTML = df.to_html(classes="table table-bordered table-striped table-sm", index=False, justify="left")
      table3.innerHTML = ""

      # Enables run program button
      document.getElementById("modify").removeAttribute("disabled")

# Replace this function with whatever function
def temp_modify(df):
   df.columns = ['C', 'B', 'A']
   df[['C', 'B', 'A']] = df[['A', 'B', 'C']]

# Downloads csv
async def dl_file(e):
  csv = df.to_csv(index=False)

  link = document.createElement('a')
  link.id = 'download-csv'
  link.setAttribute('href', 'data:text/plain;charset=utf-8,' + csv)
  link.setAttribute('download', 'data.csv')
  document.body.appendChild(link)
  document.querySelector('#download-csv').click()

async def modify_file(e):
   # Displays modified table
   global csv

   temp_modify(df)
   table1.innerHTML = "<p>Program Output here</p>"
   table3.innerHTML = df.to_html(classes="table table-bordered table-striped table-sm", index=False, justify="left")

   # Enables download button
   document.getElementById("download").removeAttribute("disabled")
   
get_file_proxy = pyodide.ffi.create_proxy(get_file)
modify_file_proxy = pyodide.ffi.create_proxy(modify_file)
# Calls dl_file whenever the download button is clicked
dl_file_proxy = pyodide.ffi.create_proxy(dl_file)

# Event listeners for buttons
document.getElementById("csv").addEventListener("change", get_file_proxy)
document.getElementById("download").addEventListener("click", dl_file_proxy)
document.getElementById("modify").addEventListener("click", modify_file_proxy)