from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Auto
from .serializers import AutoSerializer

class AutoListCreate(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class AutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [IsAuthenticated]