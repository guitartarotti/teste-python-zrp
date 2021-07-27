from bottle import route, run, response, request, get
import bottle
from sys import exit
from dateutil import tz
import time, json, sys, os

#archives
from worker import Worker
from auth import Auth

#vertices
worker = Worker()
auth = Auth()

#Consts
porta = 5000

@get('/api/pokemons/<name>')
def getAbilities(name):
    #response.content_type = 'application/json'
    #postdata = request.body.read()
    #dados = json.loads(postdata)
    #if auth.validarToken(dados['token']) == False:
        #return json.dumps({'error': 'Token invalid'})

    ability = worker.getAbilities(name)
    return json.dumps(ability)

app = bottle.app()
print(sys.argv, 'localhost:' + str(porta))
bottle.run(app=app, host='0.0.0.0', port=porta, debug=True)