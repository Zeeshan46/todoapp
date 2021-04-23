from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from todo.models import TodoItem
from todo.serializers import TodoItemSerializer


class CreateItem(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class ItemList(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class GetPutDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
