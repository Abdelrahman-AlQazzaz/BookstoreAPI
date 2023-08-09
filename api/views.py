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

class GetFilter(generics.ListAPIView):

    #permission_classes = [IsAuthenticated]
    
    serializer_class = BookSerializer

    def get_queryset(self):

        param = self.request.query_params.get('param')
        query = self.request.query_params.get('query')
        param1 = self.request.query_params.get('param1')
        query1 = self.request.query_params.get('query1')
        param2 = self.request.query_params.get('param2')
        query2 = self.request.query_params.get('query2')
        
        pqlist= [[param, query],[param1, query1],[param2, query2]]
        
        queryset = Books.objects.all()

        for pq in pqlist:
            if pq[1] is not None:
                if pq[0] == "order_by":
                    queryset = queryset.order_by(pq[1])
                elif pq[0] is not None:
                    filter_params = {pq[0]:pq[1]}
                    queryset = queryset.filter(**filter_params)
            else:
                raise Http404

        return queryset
        
class PostFilter(generics.CreateAPIView):
    
    serializer_class = BookSerializer

    def post(self, request, format=None):

        params = request.data

        queryset = Books.objects.all()

        for param_name, param_value in params.items():
            if hasattr(Books, param_name):
                if param_name == 'order_by':
                    queryset = queryset.order_by(param_value)
                else:
                    query_param = {param_name: param_value}
                    queryset = queryset.filter(**query_param)
       
        serialized = BookSerializer(queryset, many=True)

        return Response(serialized.data)