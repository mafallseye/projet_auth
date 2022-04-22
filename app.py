from flask import Flask, jsonify, request, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from routes import request_api

app = Flask(__name__)
app.config["DEBUG"] = True


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(request_api.get_blueprint())


@app.route('/login/', methods=['GET'])
def login():
    return '''<h1> Login<h1/>'''

@app.route('/register/', methods=['GET'])
def register():
    return '''<h1>Register<h1/>'''

@app.route('/auth/', methods=['GET'])
def auth():
    return '''<h1> Authentification<h1/>'''

@app.route('/dashoard', methods=['GET'])
def dashboard():
    return '''<h1>Dashboard</h1>'''

@app.route('/')
def home():
    return '''<h1>Home page</h1>'''

if __name__ == '__main__':
	app.run()