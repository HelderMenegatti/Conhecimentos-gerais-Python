from django.shortcuts import render
from rest_framework import viewsets
from .models import Books
from .serializer import BooksSerializer


class BooksSerializerViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


