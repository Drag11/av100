#!/usr/bin/python
import os
import requests
import json
from urlparse import urlparse, parse_qs

def application(environ, start_response):
    

    params = parse_qs(environ['QUERY_STRING'])

    if '/techtalon' in environ['PATH_INFO']:
        r = requests.get('https://tracker.cryptblog.ru/TDRQQd?vin=' + params['vin'][0])
        jsonresult = r.json()
    elif '/probeg' in environ['PATH_INFO']:
        r = requests.get('https://tracker.cryptblog.ru/WrNPFm?vin=' + params['vin'][0])
        jsonresult = r.json()
    else:
        r = requests.get('https://tracker.cryptblog.ru/663y12?phone=7' + params['phone'][0])
        jsonresult = r.json()
    
    
    str = json.dumps(jsonresult)

    ctype = 'application/json'
    response_headers = [('Content-Type', ctype), ('Accept', 'text/plain')]
    status = '200 OK'

    start_response(status, response_headers)


    return [str]
