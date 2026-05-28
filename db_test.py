import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)

cur = conn.cursor()
cur.execute("SELECT NOW();")
result = cur.fetchone()

print("CONNECTED:", result)

cur.close()
conn.close()