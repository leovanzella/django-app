from perfis.views import index, exibir
from django.urls import path, re_path

urlpatterns = [
    path('',                  index, name='index'),
    path('perfis/',          exibir, name='exibir'),   #r'^perfis/\d+$'
    re_path(r'^perfis/\d+$', exibir, name='exibir'),   #r'^perfis/\d+$'
]