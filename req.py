import _thread, time
import requests
from datetime import datetime
import datetime as dt
from datetime import date
from dateutil import tz
import json

class Req(object):

    def __init__(self):
        self.logs = []

    def newDate(self, time_zone):
        return str(datetime.strptime(dt.datetime.now(tz.gettz(time_zone)).strftime('%d-%m-%Y %H:%M:%S'), '%d-%m-%Y %H:%M:%S'))
    
    def sendResponse(self, obj):
        obj = json.dumps(obj)
        newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post('https://chasecapital.com.br/result', data=obj, headers=newHeaders)
        print("Status code: ", response)
        return True
    
    def newRequest(self, link):
        r = requests.get(link)
        return r