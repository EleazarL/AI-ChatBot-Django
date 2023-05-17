from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False, logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'Lo siento, no entiendo tu pregunta',
        'maximum_similarity_threshold': 0.90
    }
])

list_to_train = [
    'hola','hola como estas?'
]

list_trainer = ListTrainer(bot)

# Verificar si los datos ya están en la base de datos antes de entrenar
if not bot.storage.count():
    list_trainer.train(list_to_train)

def index(request):
    return render(request, 'chat/index.html')

def specific(request):
    number = 55
    return HttpResponse(number)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
