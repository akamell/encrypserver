from flask import Blueprint, json, jsonify, make_response, request
from flask import Flask, Response, g
#from api.Models.User import User
from functools import wraps
import datetime, hashlib, jwt, base64
from api.Helpers.Helper import Helper
from api.Helpers.Aes import Aes

mod = Blueprint('CifradoController',__name__)

@mod.route("", methods=['POST'])
def cifrarArchivo():
    fromdata = request.form
    passwd = fromdata['password']
    archivo = request.files['archivo']
    stream = archivo.stream.read()
    stream = stream.decode("utf-8")
    aes = Aes(passwd)
    resultado = aes.encrypt(stream)
    return Helper.jsonResponse(200, "Cifrado", resultado)


@mod.route("", methods=['PUT'])
def descifrarArchivo():
    fromdata = request.form
    passwd = fromdata['password']
    archivo = request.files['archivo']
    stream = archivo.stream.read().decode("utf-8") 
    print(stream)
    print(passwd)
    aes = Aes(passwd)
    resultado = aes.decrypt(stream)
    return Helper.jsonResponse(200, "Descifrado", resultado)
