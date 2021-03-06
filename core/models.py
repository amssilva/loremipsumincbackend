from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    risco = models.IntegerField()
    participantes = models.CharField(max_length=255)

    def __str__(self):
        return self.nome