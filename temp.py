import pandas as pd
import pyodide
import io
import js

table1 = Element('table1')

async def get_file(e):
    files = e.target.files.to_py()
    for file in files:
      file_content = await file.text()
      df = pd.read_csv(io.StringIO(file_content))
      table1.write(df.head())
      # table1.write(df.to_html(escape=False, classes="table"))

get_file_proxy = pyodide.ffi.create_proxy(get_file)

js.document.getElementById("csv").addEventListener("change", get_file_proxy)