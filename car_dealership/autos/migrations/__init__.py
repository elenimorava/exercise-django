from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.BrandListCreate.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', views.BrandRetrieveUpdateDestroy.as_view(), name='brand-retrieve-update-destroy'),
]