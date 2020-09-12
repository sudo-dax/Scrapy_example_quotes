import sqlite3

# Assign database connection to 'con'
con = sqlite3.connect('myquotes.db')
# Assign cursor to 'c'
c = con.cursor()

# Create Table in Database
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS quotes_tb(title TEXT, author TEXT, tag TEXT)')
# Insert Data into Table
def data_entry():
    # c.execute("""INSERT INTO quotes_tb (title, author, tag) VALUES (?, ?, ?)""")

    sql = 'INSERT INTO quotes_tb (title, author, tag) VALUES (?, ?, ?)'

    data = [
        ('do or do not there is no try', 'Yoda', 'Star Wars'),
        ('to be or not to be - that is the question', 'Shakesphere', 'Poetry'),
        ('i have a dream', 'Martin Luther King', 'Politics'),
        ('as above so below', 'Hermes Trismegustus', 'Mythology')
        ]

    con.executemany(sql, data)     
    con.commit()
    c.close()
    con.close()

# create_table()
data_entry()