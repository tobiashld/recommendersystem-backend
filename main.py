import os
from src.service.solrservice import search_film_by_name
from src.service.recommenderservice import recommend_for_movie as movieservice,recommend_for_movies as sammlungmovieservice
from flask_restful import Api, Resource
from flask import Flask,jsonify,request,abort
from flask_cors import CORS,cross_origin
import requests
import json

app = Flask(__name__)

api_v1_cors_config = {
  "origins": ["*"]
}
CORS(app, resources={"/*": api_v1_cors_config})

app.config['CORS_HEADERS'] = 'Content-Type'

def mapStringsToInt(substring):
    return int(substring)

@app.route('/', methods = ['GET'])
def mainRoute():
    return jsonify(info="hello this is an educationally used api. For more Details go to https://frontend-recommendersystem.herokuapp.com/")


@app.route('/get', methods = ['GET'])
def index():
    id = int(request.args.get("id"))
    return movieservice(id)

@app.route('/get/Sammlung', methods = ['GET'])
def getSammlung():
    print(request.args.get("ids"))
    ids = request.args.get("ids").split(" ")
    return {"result":sammlungmovieservice(ids)}


@app.route('/dropdownsearch', methods = ['GET'])
@cross_origin
def dropdownSearchRoute():
    searchtitle = str(request.args.get("searchtitle")).lower()
    return search_film_by_name(searchtitle) 


if __name__=='__main__':
    cfg_port = os.getenv('PORT', "80")
    app.run(host="0.0.0.0", port=cfg_port)
