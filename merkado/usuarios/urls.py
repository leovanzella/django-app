from usuarios.views import *
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
]