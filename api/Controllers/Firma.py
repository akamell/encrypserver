from flask import Blueprint, json, jsonify, make_response, request
from flask import Flask, Response, g

from api.Helpers.Helper import Helper
from api.Helpers.Rsa import Rsa
mod = Blueprint('FirmaController',__name__)

@mod.route("/firmar", methods=['POST'])
def cifrarArchivo():
    archivo = request.files['archivo']
    stream = archivo.stream.read()
    stream = stream.decode("utf-8")
    rsa = Rsa()
    firma = rsa.firmar(stream)
    return Helper.jsonResponse(200, "Firmado", firma.decode("utf-8"))


@mod.route("/validar", methods=['PUT'])
def descifrarArchivo():
    fromdata = request.form
    signature = fromdata['signature']
    archivo = request.files['archivo']
    stream = archivo.stream.read()
    rsa = Rsa()
    check = rsa.validar(stream, signature)
    return Helper.jsonResponse(200, "Verificacion", check)
