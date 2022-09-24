import os
from flask import Flask,jsonify
from src.service.recommenderservice import recommend_for_movie as movieservice
from flask_restful import Api, Resource

app = Flask(__name__)

api =   Api(app)

@app.route('/', methods = ['GET'])
def mainRoute():
    return jsonify(info="hello this is an educationally used api. For more Details go to https://frontend-recommendersystem.herokuapp.com/")

@app.route('/get/<id>')
def index(id):
    id = int(id)
    return movieservice(id)

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "80")
    app.run(host="0.0.0.0", port=cfg_port)#, debug=True)
    #Test
