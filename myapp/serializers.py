from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model=ProjectModel
        fields = '__all__'

class Clientserializer(serializers.ModelSerializer):
    class Meta():
        model=ClientModel
        fields='__all__'

class Todoserializer(serializers.ModelSerializer):
    class Meta():
        model=TodoList
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model=User
        fields=['id', 'username', 'first_name', 'last_name', 'email', 'password']

        extra_kwargs={'password':{
            'write_only':True,
            'required':True
        }}

    def create(self,  validated_data):
        user =User.objects.create_user(**validated_data)

        refresh = RefreshToken.for_user(user)
        token = {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
        user.token = token
        return user