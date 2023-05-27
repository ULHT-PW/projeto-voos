from django.db import models


# Create your models here.
class Aeroporto(models.Model):
    nome = models.CharField(max_length=20)
    codigo = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.nome} ({self.codigo})'


class Voo(models.Model):
    origem = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='origens')   
    destino = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='destinos') 
    duracao = models.IntegerField()

    def __str__(self):
        return f'{self.origem} - {self.destino}'


class Passageiro(models.Model):
    nome = models.CharField(max_length=20)
    voos = models.ManyToManyField(Voo, null=True, blank=True, related_name='passageiros')

    def __str__(self):
        return self.nome





