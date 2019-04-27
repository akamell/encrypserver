import os
import peewee as pw

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('/.env') / '.env'
load_dotenv(dotenv_path=env_path)


class Conexion():
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_SCHEMA = os.getenv("DB_SCHEMA")

    database = pw.PostgresqlDatabase(
        database=DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS)
    schema = DB_SCHEMA
    pw = pw
