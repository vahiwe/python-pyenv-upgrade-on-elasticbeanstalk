# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os, sys
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	# Get python version
  python_version = sys.version
  default_name = os.getenv('GAMER_NAME', 'World')
  return 'Hello, {}! I am running on Python {}!'.format(default_name, python_version)

@app.route('/health')
def health():
	return 'Healthy'

@app.route('/db')
def db():
	db_host = os.getenv('DB_HOST', 'localhost')
	db_port = os.getenv('DB_PORT', '5432')
	db_name = os.getenv('DB_NAME', 'postgres')
	db_username = os.getenv('DB_USERNAME', 'postgres')
	db_password = os.getenv('DB_PASSWORD', 'postgres')
	return 'DB INFO !\nDB_HOST: {}\nDB_PORT: {}\nDB_NAME: {}\nDB_USERNAME: {}\nDB_PASSWORD: {}\n'.format(db_host, db_port, db_name, db_username, db_password)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()