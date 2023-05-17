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
    
    # Agrega más preguntas y respuestas relacionadas con el ITTG
]


list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

#chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
#chatterbotCorpusTrainer.train('chatterbot.corpus.spanish')




def index(request):
    return render(request,'chat/index.html')

def specific(request):
    number = 55
    return HttpResponse(number)

def getResponse(request):
    #aqui vamos a obtener el mensaje del usuaruio de la funcion getResponse
    userMessage = request.GET.get('userMessage')
    #hacemos que el bot obtenga el mensaje del usuario
    chatResponse = str (bot.get_response(userMessage))
    #retornamos el mensaje
    return HttpResponse(chatResponse)
    
