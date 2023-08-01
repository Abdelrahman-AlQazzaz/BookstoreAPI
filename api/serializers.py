from rest_framework import serializers
from books.models import Books


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Books
        fields = "__all__"