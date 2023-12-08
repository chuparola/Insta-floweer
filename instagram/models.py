from django.db import models

class DadosFormulario(models.Model):
    usuario = models.CharField(max_length=100, default=False)
    email = models.EmailField(auto_created=True, default=False)
    senha = models.CharField(max_length=100, default=False)