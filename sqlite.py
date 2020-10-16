import sqlite3

conn = sqlite3.connect('users.db')

c = conn.cursor()

#c.execute("""CREATE  TABLE users(
#    first text,
#    mail text
#    )""")

c.execute("INSERT INTO users VALUES('noam' , 'noam@gmail.com')")

c.execute("SELECT * FROM users WHERE first='noam'")

print(c.fetchone())
conn.commit()

conn.close()