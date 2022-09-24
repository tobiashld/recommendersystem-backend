import requests

def search_film_by_id(id):
    api_url = "http://solrrecommendersystem.cf:8984/solr/filme/select?q=netflixid:" + str(id)
    response = requests.get(api_url)
    response_json = response.json()
    if(not response.ok):
        print('Error in "search_film_by_id" - DB-Response not ok')
    elif(not response_json.get('response').get('docs')):
        print('Error in "search_film_by_id" - no docs found for netflixid ' + str(id))        
    else:
        return response_json.get('response').get('docs')