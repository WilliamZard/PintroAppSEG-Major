def prepere_search_responses_for_account_assertion(response, account):
    '''Small helper function that formats responses from search POST endpoint to be like accounts stored in database.
    '''
    json_response = response.get_json()
    for element in json_response: 
        del element['score']
        del element['profile_type']

    for element in account['result']:
        if 'tags' in element:
            del element['tags']
    
    return json_response

def ordered(obj):
    '''Small helper function that sorts by alphabetical order all the elements in arrays 
       of dictionaries.
    '''
    if isinstance(obj, dict):
        return sorted((ordered(k), v) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj