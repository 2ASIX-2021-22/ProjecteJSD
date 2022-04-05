#!/usr/bin/env python3
import requests

idBot = '5284709102:AAG5aUAtY15hInQgPj4CybRMz9WyTkg6j6I'
idGrupo = '-778140191'

def enviarMensaje(mensaje):
    requests.post('https://api.telegram.org/bot' + idBot + '/sendMessage',
              data={'chat_id': idGrupo, 'text': mensaje, 'parse_mode': 'HTML'})

enviarMensaje("Prova resultat")