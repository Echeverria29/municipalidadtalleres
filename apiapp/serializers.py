from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User
# Serializers define the API representation.
# Se encarga de realizar el CRUD desde el API hacía la BD

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'

class TipoTallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTaller
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

