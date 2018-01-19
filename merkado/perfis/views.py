from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    #perfil = Perfil.objects.filter(email__contains='Leo')  can search for other Leos
    return render(request, 'perfil.html', {'perfil' : perfil})