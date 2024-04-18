import sqlite3
conn = sqlite3.connect('tweets.db')
c = conn.cursor()

c.execute("""CREATE TABLE people (
          user_id INTEGER primary key,
          user_name TEXT,
          user_handle TEXT,
          x_coordinate FLOAT,
          y_coordinate FLOAT,
          political_party TEXT
          year INTEGER
          )""")


conn.commit()
conn.close()