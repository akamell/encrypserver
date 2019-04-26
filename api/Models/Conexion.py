import peewee as pw

class Conexion():
	DB_NAME = "postgres"
	DB_HOST = "localhost"
	DB_PORT = "5432"
	DB_USER = "postgres"
	DB_PASS = ""
	DB_SCHEMA = "public"

	database = pw.PostgresqlDatabase(database=DB_NAME, host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS)
	schema = DB_SCHEMA
	pw = pw
