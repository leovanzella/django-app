from django.db import models

from django.db import models

class Perfil(object):
    def __init__(self, nome='', email='', telefone='', nome_empresa=''):
        self.nome = nome
        self.email = email
        self.tefefone = telefone
        self.empresa = nome_empresa
