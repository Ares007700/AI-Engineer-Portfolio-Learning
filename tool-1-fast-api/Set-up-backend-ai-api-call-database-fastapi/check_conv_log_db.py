import sqlite3
con = sqlite3.connect("app.db")
for row in con.execute("SELECT * FROM messages"):
    print(row)