from flask import Blueprint, json, jsonify, make_response, request
from flask import Flask, Response, g

from api.Helpers.Helper import Helper
from api.Helpers.Rsa import Rsa
mod = Blueprint('FirmaController',__name__)

@mod.route("/firmar", methods=['POST'])
def cifrarArchivo():
    fromdata = request.form
    archivo = request.files['archivo']
    #stream = archivo.stream.read().decode('utf-8')
    stream = archivo.stream.read()
    stream = b'ESTEESUNMENSAJECOMPADRE'
    print(stream)
    print("INUYASHA")
    rsa = Rsa()
    firma = rsa.firmar(stream)
    return Helper.jsonResponse(200, "Firmado", firma)


@mod.route("/validar", methods=['PUT'])
def descifrarArchivo():
    fromdata = request.form
    signature = fromdata['signature']
    archivo = request.files['archivo']
    stream = archivo.stream.read()
    print(stream)
    print(signature)
    rsa = Rsa()
    ok = rsa.validar(stream, signature)
    return Helper.jsonResponse(200, "Verificacion", ok)
