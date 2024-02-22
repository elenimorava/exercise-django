from django.urls import path
from . import views

urlpatterns = [
    path('autos/', views.AutoListCreate.as_view(), name='auto-list-create'),
    path('autos/<int:pk>/', views.AutoRetrieveUpdateDestroy.as_view(), name='auto-retrieve-update-destroy'),
]
