#!/bin/env python3

import requests
import json
from pprint import pprint
from urllib.parse import urlparse

def har_find_database_req():
    with open('./db.json', 'r') as f:
        har = json.loads(f.read())

        for e in har['log']['entries']:
            if e['request']['url'].endswith('/api/database'):
                return e

        raise Exception("não encontrou a chamada para /api/database")

def har_extract_headers(har_req):
    heads = {}
    for h in har_req['request']['headers']:
        heads[h['name']] = h['value']

    return heads

def req_list_databases(har_req):

    parsed_resp = json.loads(har_req['response']['content']['text'])

    dbnames = {}

    for db in parsed_resp['data']:
        dbnames[db['name']] = db['id']

    return dbnames

def req_get_baseurl(har_req):

    u = urlparse(har_req['request']['url'])
    
    return f'{u.scheme}://{u.netloc}'

def db_id_by_name(dbnames, name_search):
    for k,v in dbnames.items():
        if name_search in k:
            return v
    
    raise Exception(f"não encontrou banco com nome '{name_search}'")

ENDPOINT = '/api/dataset/csv'

if __name__ == '__main__':

    query = """

        -- DIGITE AQUI SUA CONSULTA
    """

    banco = 'nome_do_banco (pode ser parcial)'

    dbreq = har_find_database_req()
    
    dbnames = req_list_databases(dbreq)
    
    baseurl = req_get_baseurl(dbreq)
    headers = har_extract_headers(dbreq)
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    resp = requests.post(
        url = f'{baseurl}{ENDPOINT}',
        headers = headers,
        data = {
            'query': json.dumps({
                'database': db_id_by_name(dbnames, banco),
                'type': 'native',
                'native': {'query': query}
            })
        }
    )

    resp.raise_for_status()
    with open('./output.csv', 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192): 
            f.write(chunk)

    
    