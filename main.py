import os
from src.service.solrservice import search_film_by_name
from src.service.recommenderservice import recommend_for_movie as movieservice
from flask_restful import Api, Resource
from flask import Flask,jsonify,request,abort
from flask_cors import CORS,cross_origin
import requests

app = Flask(__name__)

api_v1_cors_config = {
  "origins": ["*"]
}
CORS(app, resources={"/*": api_v1_cors_config})

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods = ['GET'])
@cross_origin()
def mainRoute():
    return jsonify(info="hello this is an educationally used api. For more Details go to https://frontend-recommendersystem.herokuapp.com/")


@app.route('/get/<id>')
def index(id):
    id = int(id)
    return movieservice(id)


@app.route('/dropdownsearch', methods = ['GET'])
@cross_origin()
def dropdownSearchRoute():
    searchtitle = str(request.args.get("searchtitle")).lower()
    return search_film_by_name(searchtitle) 


if __name__=='__main__':
    cfg_port = os.getenv('PORT', "80")
    app.run(host="0.0.0.0", port=cfg_port)#, debug=True)
    #Test
