#!/usr/bin/python
import os
import requests
import json

def application(environ, start_response):
    

    print('PATH_INFO:', environ['PATH_INFO'])

    if '/probeg/' in environ['PATH_INFO']:
        vin = os.environ.get('vin')
        r = requests.get('https://tracker.cryptblog.ru/TDRQQd?vin=' + vin)
    elif environ['PATH_INFO'] == 'techtalon':
        vin = os.environ.get('vin')
        r = requests.get('https://tracker.cryptblog.ru/WrNPFm?vin=' + vin)
    else:
        phone = os.environ.get('phone')
        r = requests.get('https://tracker.cryptblog.ru/663y12?phone=7')
    
    jsonresult = r.json()
    str = json.dumps(jsonresult)

    ctype = 'application/json'
    response_headers = [('Content-Type', ctype), ('Accept', 'text/plain')]
    status = '200 OK'

    start_response(status, response_headers)


    return [str]
