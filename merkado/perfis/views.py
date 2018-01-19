from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()
    if(perfil_id == '1'):
        perfil = Perfil('Leonardo Vanzella', 'leovanzella@gmail.com', '777777', 'Oem')
    return render(request, 'perfil.html', {'perfil' : perfil})