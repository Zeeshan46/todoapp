from django.db.migrations import serializer
from rest_framework import serializers

from todo.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'