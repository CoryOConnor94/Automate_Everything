import sqlite3

# Establish connection and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

# Get all rows and columns by order
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
# print(cur.fetchall())

# Get all rows and certain columns
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
# print(cur.fetchall())

# Get all rows where asn less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
# print(cur.fetchall())

# Get all rows where asn equals 144
cur.execute("SELECT * FROM 'ips' WHERE asn = 144")
# print(cur.fetchall())

# Get all rows where asn less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
# print(cur.fetchall())

# Get all rows where asn less than 300 and domain ends in sa
cur.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
# print(cur.fetchall())

# Assign results to variable and iterate through
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
results = cur.fetchall()
for result in results:
    print(result)