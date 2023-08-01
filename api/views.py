from books.models import Books
from .serializers import BookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    '''
    Returns a list of books
    '''
    def get(self, request, format=None):
        bookList = Books.objects.all()
        serializer = BookSerializer(bookList, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Retrieve, update or delete a book instance.
    """
    def get_object(self, id):
        try:
            return Books.objects.get(id=id)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        book = self.get_object(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        book = self.get_object(id=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        book = self.get_object(id=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)