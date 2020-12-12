import sqlite3
import pandas as pd
con = sqlite3.connect("stop_covid.db")
df = pd.read_sql_query("SELECT * FROM people", con)
print(df.describe())
con.close()
