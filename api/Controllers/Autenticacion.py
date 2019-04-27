from flask import Blueprint, json, jsonify, make_response, request
from flask import Flask, Response, g

from api.Models.User import User
from functools import wraps
import datetime, hashlib, jwt, base64
from api.Helpers.Helper import Helper

mod = Blueprint('AutenticacionController',__name__)
privateKey = '#3st435L4Ll4v3Pr1V4D4C0MP4Dr3*'
JWT_ALGORITHM = 'HS256'

@mod.route("", methods=['POST'])
def login():
    jsondata = Helper.validarDataPost(request)	
    if jsondata == None:
	    return Helper.jsonResponse(400, "Json invalid "+str(jsondata), None)
    ip = request.remote_addr
    if 'username' in jsondata is False:
	    return Helper.jsonResponse(-1, "username no puede ser vacio", None)
    if 'password' in jsondata is False:
	    return Helper.jsonResponse(-2, "Password no puede ser vacio", None)
    user = jsondata.get('username','')
    passwd = jsondata.get('password','')
    if user == '':
	    return Helper.jsonResponse(-3,"Parametro invalido", None)
    if passwd == '':
	    return Helper.jsonResponse(-4,"Parametro invalido", None)

    hash_object = hashlib.sha1(passwd.encode())
    hex_dig = hash_object.hexdigest()

    usuarioValido = User.select().where(User.username == user).where(User.password == str(hex_dig)).first()
    if usuarioValido == None:
        return Helper.jsonResponse(400, "Usuario y/o password incorrecto", None)
    
    iat = datetime.datetime.now()
    uuid = Helper.generarStringUuid()
    payloadAccess = {
        'jti': uuid,
        'user_id': user,
        'exp': iat + datetime.timedelta(minutes=60),
        'iat': iat,
        'type':"access"
    }

    payloadRefresh = {
        'jti': uuid,
        'user_id': user,
        'exp': iat + datetime.timedelta(minutes=120),
        'iat': iat,
        'type':"refresh"
    }
    
    access_token = jwt.encode(payloadAccess, privateKey, JWT_ALGORITHM)
    refresh_token = jwt.encode(payloadRefresh, privateKey, JWT_ALGORITHM)
    return jsonify({"code": 200, "message": "Autenticacion correcta", "access_token": access_token.decode('UTF-8'), "refresh_token": refresh_token.decode('UTF-8')}), 200

@mod.route("/refresh", methods=['POST'])
def refreshToken():
    jsondata = Helper.validarDataPost(request)	
    if jsondata == None:
	    return Helper.jsonResponse(400, "Json invalid "+str(jsondata), None)
    ip = request.remote_addr
    if 'token' in jsondata is False:
	    return Helper.jsonResponse(-1, "Token no puede estar vacio", None)
    
    token = jsondata.get('token','')
    if token == '':
	    return Helper.jsonResponse(-2,"Parametro invalido", None)

    # decode jwt
    h,p,s = token.split(".")
    if p == '' or p == None:
        return Helper.jsonResponse(-3, "No valido", None)

    stringp = decode_base64(p)
    #parse String to Object json
    payload = {}
    try:
        payload = json.loads(stringp)			
    except ValueError as err:
        return Helper.jsonResponse(-4, "Error", None)

    userId = payload.get('user_id','')
    if userId == '':
        return Helper.jsonResponse(-5, "Error", None)
    
    typeToken = payload.get('type','')
    if typeToken != 'refresh':
        return Helper.jsonResponse(-6, "Error", None)

    iat = datetime.datetime.now()
    uuid = Helper.generarStringUuid()
    payloadAccess = {
        'jti': uuid,
        'user_id': userId,
        'exp': iat + datetime.timedelta(minutes=60),
        'iat': iat,
        'type':"access"
    }
    payloadRefresh = {
        'jti': uuid,
        'user_id': userId,
        'exp': iat + datetime.timedelta(minutes=120),
        'iat': iat,
        'type':"refresh"
    }
    
    access_token = jwt.encode(payloadAccess, privateKey, JWT_ALGORITHM)
    refresh_token = jwt.encode(payloadRefresh, privateKey, JWT_ALGORITHM)
    return jsonify({"code": 200, "message": "Refrescado con exito", "access_token": access_token.decode('UTF-8'), "refresh_token": refresh_token.decode('UTF-8')}), 200

def decode_base64(data):
    try:
        missing_padding = len(data) % 4
        if missing_padding != 0:
            data += '='* (4 - missing_padding)
        return base64.b64decode(data).decode('utf-8')
    except UnicodeDecodeError:
        return ""
