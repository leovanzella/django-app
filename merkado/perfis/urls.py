from perfis.views import *
from django.urls import path, re_path

urlpatterns = [
    path('',                  index, name='index'),
    path('perfis/',          exibir, name='exibir'),   #r'^perfis/\d+$'
    re_path(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir'),   #r'^perfis/\d+$'
    re_path(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar, name='convidar'),
]