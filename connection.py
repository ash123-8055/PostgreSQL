from dotenv import load_dotenv
import os
import psycopg2 as psy

load_dotenv()
DB_NAME=os.getenv("DATABASE")
DB_USER=os.getenv("USER_NAME")
DB_PASS=os.getenv("PASSWORD")
DB_HOST=os.getenv("SERVER_HOST")
DB_PORT=os.getenv("PORT")


conn = psy.connect(database=DB_NAME,
                   user=DB_USER,
                   password=DB_PASS,
                   host=DB_HOST,
                   port=DB_PORT
                   )

