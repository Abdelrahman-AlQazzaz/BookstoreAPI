from books.models import Books
from .serializers import BookListSerializer, BookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import HttpResponse


class BookList(APIView):
    '''
    Returns a list of books
    '''
    def get(self, request, format=None):
        bookList = Books.objects.all()
        serializer = BookListSerializer(bookList, many=True)
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
    def get_object_or_404(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object_or_404(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object_or_404(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object_or_404(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookFilter(APIView):
    """
    Filternig based on any parameter
    """
    def get(self, request, param, query, format=None):
        #return HttpResponse('bookList = Books.objects.filter(' + param + ' = "' + query + '")')
        #try:
        books = eval('Books.objects.filter(' + param + ' = query)')
        #bookList = Books.objects.filter(author = "George Orwell")
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        #except:
            #raise Http404
#class BookSearch(APIView):