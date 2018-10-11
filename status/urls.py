from django.urls import path
from .views import status, about

urlpatterns = [
    path('', status, name=''),
    path('status/', status, name='status'),
    path('about/', about, name='about'),
]