#!/usr/bin/python
import os
import requests
import json

def application(environ, start_response):

    
    vin = os.environ.get('vin')
    phone = os.environ.get('phone')

    if environ['PATH_INFO'] == '/probeg':
        r = requests.get('https://tracker.cryptblog.ru/TDRQQd?vin=' + vin)
    elif environ['PATH_INFO'] == '/techtalon':
        r = requests.get('https://tracker.cryptblog.ru/WrNPFm?vin=' + vin)
    else:
        r = requests.get('https://tracker.cryptblog.ru/663y12?phone=7')
    
    json = r.json()
    str = json.dumps(json)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)

    ctype = 'application/json'
    response_headers = [('Content-Type', ctype)]

    status = '200 OK'

    start_response(status, response_headers)


    return [binary]
