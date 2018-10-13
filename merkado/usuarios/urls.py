from usuarios.views import *
from django.conf.urls import re_path
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    re_path(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
    re_path(
        r'^login/$',
        LoginView.as_view(template_name='login.html'), name='login'
    ),
    re_path(
        r'^logout/$',
        logout_then_login, {'login_url': '/login/'}, name='logout'
    )
]
