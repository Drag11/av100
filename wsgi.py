#!/usr/bin/python
import os
import requests
import json

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

    test1 = r.encode('utf-8') 
    response_headers = [('Content-Type', ctype)]

    status = '200 OK'

    start_response(status, response_headers)

    return [test1]
