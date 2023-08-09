from typing import Any
from books.models import Books, Authors, Genres, Publishers
from .serializers import BookListSerializer, BookSerializer, AuthorSerializer, GenreSerializer, PublisherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
#from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
    
class BookList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Books.objects.all()
    serializer_class = BookSerializer
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class AuthorList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer

class GenreList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

class PublisherList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Publishers.objects.all()
    serializer_class = PublisherSerializer
class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Publishers.objects.all()
    serializer_class = PublisherSerializer
        
class BookFilter(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

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
    
class AuthorFilter(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        params = request.data

        queryset = Authors.objects.all()

        for param_name, param_value in params.items():
            if hasattr(Authors, param_name):
                if param_name == 'order_by':
                    queryset = queryset.order_by(param_value)
                else:
                    query_param = {param_name: param_value}
                    queryset = queryset.filter(**query_param)
       
        serialized = AuthorSerializer(queryset, many=True)

        return Response(serialized.data)
    
class GenreFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self): 
        param = self.request.query_params.get('param') 
        query = self.request.query_params.get('query') 
        param1 = self.request.query_params.get('param1') 
        query1 = self.request.query_params.get('query1') 
        param2 = self.request.query_params.get('param2') 
        query2 = self.request.query_params.get('query2') 
        pqlist= [[param, query],[param1, query1],[param2, query2]] 
        queryset = Genres.objects.all() 
        for pq in pqlist: 
            if pq[1] is not None: 
                if pq[0] == "order_by": queryset = queryset.order_by(pq[1]) 
                elif pq[0] is not None: filter_params = {pq[0]:pq[1]} 
                queryset = queryset.filter(**filter_params) 
            else: raise Http404 
        return queryset
        
class PublisherFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self): 
        param = self.request.query_params.get('param') 
        query = self.request.query_params.get('query') 
        param1 = self.request.query_params.get('param1') 
        query1 = self.request.query_params.get('query1') 
        param2 = self.request.query_params.get('param2') 
        query2 = self.request.query_params.get('query2') 
        pqlist= [[param, query],[param1, query1],[param2, query2]] 
        queryset = Publishers.objects.all() 
        for pq in pqlist: 
            if pq[1] is not None: 
                if pq[0] == "order_by": queryset = queryset.order_by(pq[1]) 
                elif pq[0] is not None: filter_params = {pq[0]:pq[1]} 
                queryset = queryset.filter(**filter_params) 
            else: raise Http404 
        return queryset
    