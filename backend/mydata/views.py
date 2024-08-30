from rest_framework import generics
from rest_framework import permissions
from auth.permissions import IsCreatorOrAdmin

from .models import Mydata
from .serializers import MydataSerializer 

class ListCreateMydata(generics.ListCreateAPIView):
    queryset  = Mydata.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsCreatorOrAdmin]
    serializer_class = MydataSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Mydata.objects.filter(user=self.request.user)
        else:
            return Mydata.objects.all()

class RetrieveUpdateDestroyMydata(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Mydata.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsCreatorOrAdmin]
    serializer_class = MydataSerializer