import requests

def search_film_by_id(id):
    api_url = "http://solrrecommendersystem.cf:8984/solr/filme/select?q=netflixid:"+ str(id)
    response = requests.get(api_url)
    response_json = response.json()
    if(response.ok and response_json.get('response').get('docs')):
        return response_json.get('response').get('docs')
    else:   
        print('Error in "search_film_by_id" - Problem with DB-Response')

#response = search_film_by_id(1)
#print(response)

