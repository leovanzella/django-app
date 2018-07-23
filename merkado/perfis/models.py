from django.db import models
from django.contrib.auth.models import User
from .abtest import ABTest

class Perfil(models.Model):

    nome = models.CharField(max_length=255, null=False)
    #email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)

    contatos = models.ManyToManyField('self')

    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='perfil')

    # def save(self, **kwargs):
    #     pass
    #     # super(ABTest, self).save(**kwargs)
    #     # ab_test = ABTest(True)
    #     # ab_test.save()


    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()
