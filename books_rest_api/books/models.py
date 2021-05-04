from django.db import models

# Create your models here.

class Books(models.Model):
    """Faz o cadastro dos livivros"""
    Titulo = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=25)
    Autor = models.CharField(max_length=250)
    Editora = models.CharField(max_length=250)
    Edicao = models.CharField(max_length=250)
    Numero_de_paginas = models.IntegerField()
    Descricao_rapida = models.CharField(max_length=300, null=True)


    """Retorna a representação do modelo de string." """
    def __str__(self):
        return f"{self.Titulo}, {self.ISBN}, {self.Autor}," \
               f" {self.Editora}, {self.Edicao}, {self.Numero_de_paginas}, " \
               f"{self.Descricao_rapida}"
