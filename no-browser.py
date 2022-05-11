import pandas as pd
from pprint import PrettyPrinter


pp = PrettyPrinter(indent=4)
df = pd.read_html("table.html")[0]

pp.pprint(
    df[["Server Name", "Host", "Port"]].to_json(
        "./ftp-table.json", orient="table", index=False
    )
)

writer = pd.ExcelWriter("ftp-table.xlsx", engine="xlsxwriter")
df.to_excel(writer, index=False)
writer.save()
