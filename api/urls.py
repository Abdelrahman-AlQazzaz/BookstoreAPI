from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.BookList.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('filter/<param>/<query>/', views.BookFilter.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)