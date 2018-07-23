from django.db import models

class ABTest(models.Model):

    id = models.IntegerField(primary_key=True)
    ab_test_type = models.BooleanField(u'imagem adicional', default=False)
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='ab_test')

