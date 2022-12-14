from flask import abort
import requests



def search_film_by_id(id):
    api_url = "http://solrrecommendersystem.cf:8984/solr/filminfos/select?q=netflixid:" + str(id)
    response = requests.get(api_url)
    response_json = response.json()
    if(not response.ok):
        print('Error in "src.service.solrservice.search_film_by_id" - DB-Response not ok')
    elif(not hasattr(response_json.get('response'),"docs") and not response_json.get('response').get('docs') and len(response_json.get('response').get('docs')) <= 0):
        print('Error in "src.service.solrservice.search_film_by_id" - no docs found for netflixid ' + str(id))        
    else:

        return response_json.get('response').get('docs')[0]
        
def search_film_by_ids(ids):
    ids = [str(x) for x in ids]
    ids = '%20'.join(ids)
    api_url = "http://solrrecommendersystem.cf:8984/solr/filminfos/select?q=netflixid:(" + ids + ")"
    response = requests.get(api_url)
    response_json = response.json()
    if(not response.ok):
        print('Error in "src.service.solrservice.search_film_by_id" - DB-Response not ok')
    elif(not hasattr(response_json.get('response'),"docs") and not response_json.get('response').get('docs') and len(response_json.get('response').get('docs')) <= 0):
        print('Error in "src.service.solrservice.search_film_by_id" - no docs found for netflixid ' + str(id))        
    else:
        return response_json.get('response').get('docs')

def search_film_by_name(searchtitle):
    endsuchstring = ""
    for word in searchtitle.split(" "):
        endsuchstring += "*"+word+"*"
    api_url =  "http://solrrecommendersystem.cf:8984/solr/filminfos/select?q=searchtitle%3A"+endsuchstring+"&q.op=OR&rows=25"
    response = requests.get(api_url)
    if response.status_code == 200 and hasattr(response,"text"): #and response.text > 0:
        return response.json()     
    else:
        abort(404)

solrservice = {
    search_film_by_id,
    search_film_by_ids,
    search_film_by_name
}