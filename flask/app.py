import os
from flask import Flask

app = Flask(__name__)

@app.route('/about',methods=['GET'])
def about():
    version = os.environ.get('APP_VERSION')

    return {'version':version}, 200

@app.route('/secrets',methods=['GET'])
def secrets ():
    creds = dict()

    creds['db_password'] = os.environ.get('DB_PASSWORD')
    creds['api_secret'] = open("/run/secrets/api_key","r").read()

    return creds, 200