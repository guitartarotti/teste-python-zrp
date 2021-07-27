from datetime import datetime
import datetime as dt
from datetime import date
import pandas as pd, _thread, json
from req import Req

#Requests to PokemonAPI
req = Req()


class Worker(object):

    def __init__(self):
        self.logs = []

    def getAbilities(self, name):
        try:
            link = 'https://pokeapi.co/api/v2/pokemon/'+name
            response = self.newRequest(link)
            content = response.json()

            terms = content['abilities']

            li = [item['ability'].get('name') for item in terms]

            return sorted(li)
        except Exception as error:
            try:
                print('Erro ao processar', name)
                self.logs.append('Process Error|'+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'|'+name)
            finally:
                print('Erro', error)

    def abilities(self, name):
        _thread.start_new_thread(self.getAbilities, (name))

    def newRequest(self, name):
        print('Nova Requisicao', name)
        self.logs.append('New Request|'+dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'|'+name)
        response = req.newRequest(name)
        return response