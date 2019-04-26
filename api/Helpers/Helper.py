from flask import json, jsonify
import datetime, re, hashlib, random

class Helper():

	@staticmethod
	def jsonResponse(code, message, data):
		codeResponse = 400
		if code >= 200 and code <= 299:
			codeResponse = 200
		elif code < 0:			
			codeResponse = 400
		else:			
			codeResponse = code

		return jsonify({"code":code, "message": message, "data": data}), codeResponse

	@staticmethod
	def validarDataPost(request):
		fromdata = request.data
		if fromdata == "" or fromdata == None:
			return -1
		try:
			#Convertimos las cadena a objeto json
			obj = json.loads(fromdata)
			return obj
		except ValueError as err:
			return -2

	@staticmethod
	def generarStringUuid():		
		codeUuid=str(random.randint(0000000, 9999999))+"-"+str(random.randint(0000, 9999))+"-"+str(random.randint(0000, 9999))+"-"+str(random.randint(0000, 9999))+"-"+str(random.randint(000000000000, 999999999999))
		return codeUuid

	@staticmethod
	def getStringSession():
		codeString = Helper.getCadenaRandom(7)+Helper.getCadenaRandom(4)+Helper.getCadenaRandom(4)+Helper.getCadenaRandom(4)+Helper.getCadenaRandom(12)
		return codeString

	@staticmethod
	def getCadenaRandom(size):
		string = ""
		for x in range(0, size):
			abc = "ABCDEFGHIJKLMNOPQRSTUVWKYZ"
			letterOrNumber = random.randint(0,1)

			#Inicialmente Letra sera un numero alatorio de 0 a 9
			letra = random.randint(0,9)
			#si es 1 entonces sera una letra
			if letterOrNumber == 1:
				#Se rifa la letra a escoger
				letraPos = random.randint(0,25)			
				letra = abc[letraPos]
				#Se rifa si sera UPPER o Lower
				numberCase =random.randint(0,1)
				if numberCase == 1:
					letra = letra.lower()
				string = string + letra
			else:
				string = string + str(letra)

		return string
