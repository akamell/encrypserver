from peewee import *
from api.Models.Conexion import Conexion
import datetime

con = Conexion()

class User(con.pw.Model):
    id=con.pw.AutoField(primary_key = True)
    username=con.pw.CharField(max_length=50)
    password=con.pw.CharField(max_length=100)
    nombre=con.pw.CharField(max_length=50)
    apellido=con.pw.CharField(max_length=50)    

    class Meta:
	    database = con.database
	    db_table = 'user'
	    schema = con.schema

if __name__ == '__main__':
	print("Creada model user")
	User.create_table()
