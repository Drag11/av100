#!/usr/bin/python
import os
import requests

def application(environ, start_response):

    ctype = 'application/json'
    vin = os.environ['vin']
    if environ['PATH_INFO'] == '/probeg':
        r = requests.get('https://tracker.cryptblog.ru/TDRQQd?vin=' + vin)
    elif environ['PATH_INFO'] == '/techtalon':
        r = requests.get('https://tracker.cryptblog.ru/WrNPFm?vin=' + vin)
    else:
        phone = os.environ['phone']
        r = requests.get('https://tracker.cryptblog.ru/663y12?phone=7' + phone)
    
    r.json()

    response.out.write(r.dumps(response))
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]

    status = '200 OK'

    start_response(status, response_headers)

    return [response_body]
