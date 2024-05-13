from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    senha = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.nome
