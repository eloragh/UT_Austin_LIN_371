import sqlite3
conn = sqlite3.connect('tweets.db')
c = conn.cursor()

c.execute("""CREATE TABLE tweets (
          user_id INTEGER primary key,
          user_name TEXT,
          user_handle TEXT,
          tweet_id INTEGER,
          tweet_text TEXT,
          created_date DATETIME
          )""")


conn.commit()
conn.close()
