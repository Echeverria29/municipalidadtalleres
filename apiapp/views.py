from django.shortcuts import render

# Create your views here.

from ssl import VERIFY_DEFAULT
from django.shortcuts import render
from app.models import *
from .serializers import *
from rest_framework import viewsets



class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer

class TipoTallerViewSet(viewsets.ModelViewSet):
    queryset = TipoTaller.objects.all()
    serializer_class = TipoTallerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



