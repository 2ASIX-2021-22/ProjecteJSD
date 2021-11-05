#!/bin/python
import requests
import sys
from shodan import Shodan
import socket
# Demana a l'usuari una ip que la guardara en la variable dades.
dades = input("Disme la ip que vols buscar: ")
# Setup de API de (Sergi)
api = Shodan('iyw7Is1pCQ2kCoqAn6KNEQvpT2VlqBpo')

# Crearem dos variables una que guardarem la informació del equip que està a l'API de Shodan.
results = api.search(dades)             
# Bucle que recorre la informació de l'API:
for result in results['matches']:
    data = {
        # "asn": result['asn'],
        # "ip": result['ip'],
        "IP": result['ip_str'],
        "Port": socket.getservbyport(result['port']),
        # "timestamp": result['timestamp'],
        # "hostnames": [
        #     result['hostnames']
        # ],
        "domains": [
             result['domains']
        ]
        # "location": {
        #     "city": result['location']['city'],
        #     "country_code": result['location']['country_code'],
        #     "country_code3": result['location']['country_code3'],
        #     "country_name": result['location']['country_name'],
        #     "dma_code": result['location']['dma_code'],
        #     "latitude": result['location']['latitude'],
        #     "longitude": result['location']['longitude'],
        #     "postal_code": result['location']['postal_code'],
        #     "region_code": result['location']['region_code']
        # },  
        # "org": result['org'],
        # "isp": result['isp'],
        # "os": result['os'],
        # "transport": result['transport'],
        # "data": result['data']
    }
    print(data)
