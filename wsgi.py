#!/usr/bin/python
import os
import requests
import json
from urlparse import urlparse, parse_qs

def application(environ, start_response):
    

    params = parse_qs(environ['QUERY_STRING'])  #  Here you get the values in a dict!
    print params

    if '/probeg' in environ['PATH_INFO']:
        r = requests.get('https://tracker.cryptblog.ru/TDRQQd?vin=' + params['vin'])
    elif '/techtalon' in environ['PATH_INFO']:
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
