from flask import Flask, g, request, json
from flask_cors import CORS

from api.Helpers.Helper import Helper

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, allow_headers='Accept, Content-Type, Authorization', methods=['GET','POST','PUT','DELETE'])

from api.Controllers.Autenticacion import mod
from api.Controllers.Registro import mod
from api.Controllers.Cifrado import mod
from api.Controllers.Firma import mod

app.register_blueprint(Controllers.Autenticacion.mod, url_prefix='/api/auth')
app.register_blueprint(Controllers.Registro.mod, url_prefix='/api/registro')
app.register_blueprint(Controllers.Cifrado.mod, url_prefix='/api/cifrado')
app.register_blueprint(Controllers.Firma.mod, url_prefix='/api/firma')

@app.before_request
def before_request():
	g.token = request.headers.get('Authorization','')
	g.endpoint = request.endpoint
	method = request.method
	if method == 'OPTIONS':
		return Helper.jsonResponse(200,"options methods ", None)

@app.after_request
def after_request(response):	
	response.headers.add('Access-Control-Allow-Origin','*')
	response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization')
	response.headers.add('Access-Control-Allow-Methods','GET,POST,PUT,DELETE,OPTIONS')
	# response.headers.add('Server','')
	return response
