from django.urls import path
from .views import status, about, delete

urlpatterns = [
    path('', status, name=''),
    path('status/', status, name='status'),
    path('about/', about, name='about'),
    path('delete-all/', delete, name='delete'),
]