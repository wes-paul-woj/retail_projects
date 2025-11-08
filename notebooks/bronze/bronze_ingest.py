import pandas as pd, io, requests

url = "https://raw.githubusercontent.com/databricks-datasets/retail-org/main/sales_orders/part-00000-tid-3380907111862188800-1b2b6a49-9f4d-4c12-9d90-1d3fa17ad6e0-256-c000.csv"
csv_data = requests.get(url).text
pdf = pd.read_csv(io.StringIO(csv_data))

display(pdf.head())
