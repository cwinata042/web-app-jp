import pandas as pd
import pyodide
import io
from js import document

table1 = document.getElementById('table1')
table2 = document.getElementById('table2')
table3 = document.getElementById('table3')
csv = ''

async def get_file(e):
    files = e.target.files.to_py()
    for file in files:
      global csv
      file_content = await file.text()
      df = pd.read_csv(io.StringIO(file_content))

      # Displays original table
      table1.innerHTML = df.to_html(classes="table table-bordered table-striped table-sm", index=False, justify="left")

      # Displays modified tables
      temp_modify1(df)
      table2.innerHTML = df.to_html(classes="table table-bordered table-striped table-sm", index=False, justify="left")
      temp_modify2(df)
      table3.innerHTML = df.to_html(classes="table table-bordered table-striped table-sm", index=False, justify="left")

      # Saves modified df in .csv format to csv
      csv = df.to_csv(index=False)

      document.getElementById("download").removeAttribute("disabled")

# Replace this function with whatever function
def temp_modify1(df):
   df.columns = ['C', 'B', 'A']
   df[['C', 'B', 'A']] = df[['A', 'B', 'C']]

# Replace this funcion with whatever function
def temp_modify2(df):
   df.columns = ['C', 'B', 'A']
   df[['C', 'B', 'A']] = df[['A', 'C', 'B']]

# Downloads csv
async def dl_file(e):
  link = document.createElement('a')
  link.id = 'download-csv'
  link.setAttribute('href', 'data:text/plain;charset=utf-8,' + csv)
  link.setAttribute('download', 'data.csv')
  document.body.appendChild(link)
  document.querySelector('#download-csv').click()
   
get_file_proxy = pyodide.ffi.create_proxy(get_file)
# Calls dl_file whenever the download button is clicked
dl_file_proxy = pyodide.ffi.create_proxy(dl_file)

# Event listeners for buttons
document.getElementById("csv").addEventListener("change", get_file_proxy)
document.getElementById("download").addEventListener("click", dl_file_proxy)