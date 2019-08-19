from django.shortcuts import render
from core.models import Evento

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'agenda/agenda.html', {'eventos':eventos})