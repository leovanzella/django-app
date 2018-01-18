from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    return render(request, 'perfil.html')