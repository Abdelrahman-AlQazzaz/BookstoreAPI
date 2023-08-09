from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
#from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),

    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),

    path('publishers/', views.PublisherList.as_view()),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view()),

    path('genres/', views.GenreList.as_view()),
    path('genres/<int:pk>/', views.GenreDetail.as_view()),

    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/filter/', views.BookFilter.as_view()),
    path('genres/filter/', views.GenreFilter.as_view()),
    path('publishers/filter/', views.PublisherFilter.as_view()),
    path('authors/filter/', views.AuthorFilter.as_view())


]

urlpatterns = format_suffix_patterns(urlpatterns)