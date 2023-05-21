from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Inicializar el chatbot
bot = ChatBot('chatbot', read_only=False, logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'Lo siento, no entiendo tu pregunta',
        'maximum_similarity_threshold': 0.90
    }
])

# Entrenar el chatbot con corpus de texto en español
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.spanish')

# Lista de preguntas y respuestas
preguntas_respuestas = [
    ('¿Cuál es tu nombre?', 'Mi nombre es ChatBot'),
    ('¿Cómo estás?', 'Estoy bien, gracias'),
    # Agrega más preguntas y respuestas aquí
]

# Entrenar el chatbot con preguntas y respuestas manualmente
list_trainer = ListTrainer(bot)
for pregunta, respuesta in preguntas_respuestas:
    list_trainer.train([pregunta, respuesta])

# Vista de la página de inicio
def index(request):
    return render(request, 'chat/index.html')

# Vista para una ruta específica
def specific(request):
    number = 55
    return HttpResponse(number)

# Vista para obtener una respuesta del chatbot
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
