def prepere_search_responses_for_account_assertion(response):
    '''Small helper function that formats responses from search POST endpoint to be like accounts stored in database.
        It removes the score and profile type fields and makes sure to propely format the tags field.
    '''
    json_response = response.get_json()
    for element in json_response: 
        del element['score']
        del element['profile_type']
        #format tag field
        if 'tags' in element:
            if isinstance(element['tags'], list):
                element['tags'] = element['tags'][1:1]
            else:
                element['tags'] = element['tags'].split()[1:1]
        if 'team_members' in element:
            if isinstance(element['team_members'], list):
                element['team_members'] = element['team_members'][1:1]
            else:
                element['team_members'] = element['team_members'].split()[1:1]

    
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