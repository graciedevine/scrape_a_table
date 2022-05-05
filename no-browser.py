import pandas as pd
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
df = pd.read_html("table.html")[0]
print(df)

pp.pprint(df[["Server Name", "Host", "Port"]].to_json(orient="index", index=False))
