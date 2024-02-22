from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
]
