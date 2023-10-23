import pandas as pd
import pyodide
import io
from js import document

table1 = document.getElementById('table1')
table2 = document.getElementById('table2')
table3 = document.getElementById('table3')

async def get_file(e):
    files = e.target.files.to_py()
    for file in files:
      file_content = await file.text()
      df = pd.read_csv(io.StringIO(file_content))

      # Displays original table
      table1.innerHTML = df.to_html(classes="table", index=False)

      # Displays modified tables
      temp_modify1(df)
      table2.innerHTML = df.to_html(classes="table", index=False)
      temp_modify2(df)
      table3.innerHTML = df.to_html(classes="table", index=False)

def temp_modify1(df):
   df.columns = ['C', 'B', 'A']
   df[['C', 'B', 'A']] = df[['A', 'B', 'C']]

def temp_modify2(df):
   df.columns = ['C', 'B', 'A']
   df[['C', 'B', 'A']] = df[['A', 'C', 'B']]

get_file_proxy = pyodide.ffi.create_proxy(get_file)

js.document.getElementById("csv").addEventListener("change", get_file_proxy)
# TO-DO: Handle downloading a dataframe into .csv file
#       Allow selecting file path
# js.document.getElementById('download').addEventListener("onClick", downloadFile)