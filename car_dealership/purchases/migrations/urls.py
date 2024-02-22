from django.urls import path
from . import views

urlpatterns = [
    path('purchases/', views.PurchaseListCreate.as_view(), name='purchase-list-create'),
    path('purchases/<int:pk>/', views.PurchaseRetrieveUpdateDestroy.as_view(), name='purchase-retrieve-update-destroy'),
]