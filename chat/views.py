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
    "¿Qué es el ITTG?",
    "El ITTG es el Instituto Tecnológico de Tuxtla Gutiérrez, una institución educativa de nivel superior ubicada en Chiapas, México.",
    "¿Cuáles son las carreras que ofrece el ITTG?",
    "El ITTG ofrece carreras en áreas como Ingeniería en Sistemas Computacionales, Ingeniería Industrial, Ingeniería Electrónica, Ingeniería en Gestión Empresarial, entre otras.",
    "¿Dónde se encuentra ubicado el ITTG?",
    "El ITTG se encuentra en Tuxtla Gutiérrez, Chiapas, México.",
    "¿Cuál es el enfoque educativo del ITTG?",
    "El ITTG tiene un enfoque educativo orientado a la formación integral de los estudiantes, combinando conocimientos teóricos con prácticos y promoviendo la participación en proyectos.",
    "¿El ITTG ofrece programas de posgrado?",
    "Sí, el ITTG ofrece programas de posgrado en diferentes áreas de estudio.",
    "¿Cuáles son los requisitos de admisión al ITTG?",
    "Los requisitos de admisión al ITTG pueden variar dependiendo de la carrera y el proceso de selección. Es recomendable consultar la convocatoria oficial del ITTG para obtener información precisa sobre los requisitos.",
    "¿El ITTG cuenta con programas de intercambio estudiantil?",
    "Sí, el ITTG tiene convenios de intercambio estudiantil con diversas instituciones nacionales e internacionales.",
    "¿El ITTG ofrece becas?",
    "Sí, el ITTG cuenta con programas de becas y apoyos económicos para los estudiantes.",
    "¿Cuál es el proceso de titulación en el ITTG?",
    "El proceso de titulación en el ITTG puede variar dependiendo de la carrera y la modalidad de titulación.",
    "¿El ITTG tiene convenios de colaboración con empresas?",
    "Sí, el ITTG tiene convenios de colaboración con diversas empresas e instituciones.",
    "¿Cuáles son las instalaciones disponibles en el ITTG?",
    "El ITTG cuenta con diversas instalaciones que incluyen aulas, laboratorios, biblioteca, áreas deportivas y espacios de convivencia estudiantil.",
    "¿El ITTG ofrece programas de vinculación con la industria?",
    "Sí, el ITTG tiene programas de vinculación con la industria que permiten establecer lazos con empresas y sectores productivos.",
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
    
