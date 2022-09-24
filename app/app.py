import os
from flask import Flask,jsonify,request,abort
from flask_restful import Api, Resource
from flask_cors import CORS
#from flask_cors import Flask,jsonify,request
import requests

app = Flask(__name__)
CORS(app)
api =   Api(app)

@app.route('/', methods = ['GET'])
def mainRoute():
    return jsonify(info="hello this is an educationally used api. For more Details go to https://frontend-recommendersystem.herokuapp.com/")

@app.route('/dropdownsearch', methods = ['GET'])
def dropdownSearchRoute():
    searchtitle = str(request.args.get("searchtitle")).lower()
    endsuchstring = ""
    for word in searchtitle.split("+"):
      endsuchstring += "*"+word+"*"
    api_url =  "http://solrrecommendersystem.cf:8984/solr/filme/select?q=searchtitle%3A"+endsuchstring+"&q.op=OR&rows=3"
    response = requests.get(api_url)
    if response.status_code == 200 and hasattr(response,"text"): #and response.text > 0:
        return jsonify(response.text)        
    else:
        abort(404)

    


if __name__=='__main__':
    cfg_port = os.getenv('PORT', "80")
    app.run(host="0.0.0.0", port=cfg_port)#, debug=True)
    #Test
