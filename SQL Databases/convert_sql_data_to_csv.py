import sqlite3
import pandas as pd

# Establish connection and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

df = pd.read_sql("SELECT * FROM 'ips' ORDER BY asn", con)

df.to_csv('database.csv', index=None)
