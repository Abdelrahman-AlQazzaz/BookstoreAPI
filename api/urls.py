from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
#from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('<model>/', views.Main.as_view()),
    path('<model>/<int:pk>/', views.Detail.as_view()),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<model>/filter/<str:param>/<str:query>/', views.Filter.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)