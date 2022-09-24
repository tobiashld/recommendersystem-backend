import requests

def search_film_by_id(id):
    api_url = "http://solrrecommendersystem.cf:8984/solr/filme/select?q=netflixid:" + str(id)
    response = requests.get(api_url)
    response_json = response.json()
    if(not response.ok):
        print('Error in "src.service.solrservice.search_film_by_id" - DB-Response not ok')
    elif(not hasattr(response_json.get('response'),"docs") and not response_json.get('response').get('docs') and len(response_json.get('response').get('docs')) <= 0):
        print('Error in "src.service.solrservice.search_film_by_id" - no docs found for netflixid ' + str(id))        
    else:
        print(len(response_json.get('response').get('docs')))
        return response_json.get('response').get('docs')[0]