from flask import Blueprint, json, jsonify, make_response, request
from flask import Flask, Response, g
#from api.Models.User import User
from functools import wraps
import datetime, hashlib, jwt, base64
from api.Helpers.Helper import Helper

mod = Blueprint('RegistroController',__name__)

@mod.route("", methods=['POST'])
def registrar():
    jsondata = Helper.validarDataPost(request)	
    if jsondata == None:
	    return Helper.jsonResponse(400, "Json invalid "+str(jsondata), None)
    ip = request.remote_addr
    if 'username' in jsondata is False:
	    return Helper.jsonResponse(-1, "username no puede ser vacio", None)
    if 'password' in jsondata is False:
	    return Helper.jsonResponse(-2, "Password no puede ser vacio", None)
    if 'nombre' in jsondata is False:
	    return Helper.jsonResponse(-3, "Password no puede ser vacio", None)
    if 'apellido' in jsondata is False:
	    return Helper.jsonResponse(-4, "Password no puede ser vacio", None)
    
    user = jsondata.get('username','')
    passwd = jsondata.get('password','')
    nombre = jsondata.get('nombre','')
    apellido = jsondata.get('apellido','')

    if user == '':
	    return Helper.jsonResponse(-5,"Parametro invalido", None)
    if passwd == '':
	    return Helper.jsonResponse(-6,"Parametro invalido", None)
    if nombre == '':
        return Helper.jsonResponse(-7,"Parametro invalido", None)
    if apellido == '':
        return Helper.jsonResponse(-8,"Parametro invalido", None)

    hash_object = hashlib.sha1(passwd.encode())
    hex_dig = hash_object.hexdigest()
    data = {
        "user": user,
        "passwd": passwd,
        "nombre": nombre,
        "apellido": apellido,
        "sha1": str(hex_dig)
    }
    return Helper.jsonResponse(200, "Exito", data)
