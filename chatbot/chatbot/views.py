from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from chatbot import Chatbot

def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chatview.html')

@csrf_exempt
def get_response(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']
        bot = Chatbot()
        chat_response = bot.get_response(message)
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
        response['status'] = 'ok'
    else:
        response['error'] = 'Keine POST Daten gefunden'
    return HttpResponse(json.dumps(response), content_type="application/json" )

