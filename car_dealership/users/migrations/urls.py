from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListCreate.as_view(), name='user-list-create'),
    path('<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
]