import sqlite3

# Establish connection and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

new_rows = [
    ('100.100.99.22', 'example.com', 144),
    ('192.178.17.42', 'example.local', 33)
]

cur.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
con.commit()

cur.execute("SELECT * FROM 'ips'")
print(cur.fetchall())
