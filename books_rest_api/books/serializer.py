from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:

        model = Books
        fields = ['Titulo','ISBN',
                  'Autor','Editora',
                  'Edicao', 'Numero_de_paginas',
                  'Descricao_rapida',
                  ]