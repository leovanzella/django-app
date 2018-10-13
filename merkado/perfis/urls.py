from perfis.views import *
from django.urls import path, re_path

urlpatterns = [
    path('',                  index, name='index'),
    path('perfis/',          exibir, name='exibir'),
    re_path(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir'),
    re_path(r'^perfis/(?P<perfil_id>\d+)/convidar$', convidar, name='convidar'),
    re_path(r'^convite/(?P<convite_id>\d+)/aceitar$', aceitar, name='aceitar'),
]
