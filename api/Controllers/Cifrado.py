from flask import Blueprint, json, jsonify, make_response, request
from flask import Flask, Response, g
#from api.Models.User import User
from functools import wraps
import datetime, hashlib, jwt, base64
from api.Helpers.Helper import Helper
from api.Helpers.Aes import Aes

mod = Blueprint('CifradoController',__name__)

@mod.route("archivo", methods=['POST'])
def cifrarArchivo():
    jsondata = Helper.validarDataPost(request)	
    if jsondata == None:
	    return Helper.jsonResponse(400, "Json invalid "+str(jsondata), None)
    ip = request.remote_addr
    if 'archivo' in jsondata is False:
	    return Helper.jsonResponse(-1, "username no puede ser vacio", None)
    if 'password' in jsondata is False:
	    return Helper.jsonResponse(-2, "Password no puede ser vacio", None)

    archivo = jsondata.get('archivo','')
    if archivo == '':
        return Helper.jsonResponse(-3, "Error parametro no valido", None)
    passwd = jsondata.get('password','')
    if passwd == '':
        return Helper.jsonResponse(-4, "Error parametro no valido", None)
    
    aes = Aes("P1ssw0rd2")
    resultado = aes.encrypt(archivo)
    
    return Helper.jsonResponse(200, "Cifrado", resultado)
