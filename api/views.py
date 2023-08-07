from typing import Any
from books.models import Books, Authors, Genres, Publishers
from .serializers import BookListSerializer, BookSerializer, AuthorSerializer, GenreSerializer, PublisherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
#from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
class Views(APIView):

    def get_model_serializer(self, model):
        if model == 'books':
            return [Books, BookSerializer, BookListSerializer]
        elif model == 'authors':
            return [Authors, AuthorSerializer]
        elif model == 'genres':
            return [Genres, GenreSerializer]
        elif model == 'publishers':
            return [Publishers, PublisherSerializer]
        else:
            raise Http404

class Main(Views):
    '''
    Returns a list of books & allows for posting new instances
    '''
    
    def get(self, request, model, format=None):
        ms = self.get_model_serializer(model)
        Model = ms[0]
        ListSerializer = ms[-1]
        bookList = Model.objects.all()
        serializer = ListSerializer(bookList, many=True)
        return Response(serializer.data)
    
    def post(self, request, model, format=None):
        ms = self.get_model_serializer(model)
        DetailSerializer = ms[1]
        serializer = DetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Detail(Views):
    """
    Retrieve, update or delete a book instance.
    """

    def get_object_or_404(self, model, pk):
        ms = self.get_model_serializer(model)
        Model = ms[0]
        try:
            return Model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, model, pk, format=None):
        ms = self.get_model_serializer(model)
        DetailSerializer = ms[1]

        book = self.get_object_or_404(model, pk)
        serializer = DetailSerializer(book)
        return Response(serializer.data)

    def put(self, request, model, pk, format=None):
        ms = self.get_model_serializer(model)
        DetailSerializer = ms[1]

        book = self.get_object_or_404(model, pk)
        serializer = DetailSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, model, pk, format=None):
        book = self.get_object_or_404(model, pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Filter(Views):
    #permission_classes = [IsAuthenticated]
    """
    Filternig based on any parameter
    """
    def get(self, request, model, param, query, format=None):  
        ms = self.get_model_serializer(model)
        Model = ms[0]
        DetailSerializer = ms[1]

        if query == '_ascending_':
            books = Model.objects.all().order_by(str(param))
        elif query == '_descending_':
            books = Model.objects.all().order_by("-" + str(param))
        else:
            filter_params = {param: query}
            books = Model.objects.filter(**filter_params)
        serializer = DetailSerializer(books, many=True)
        return Response(serializer.data)