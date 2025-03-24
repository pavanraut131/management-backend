from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate
from rest_framework.views import APIView

# Create your views here.


class ClientView(viewsets.ModelViewSet):
    serializer_class= Clientserializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get_queryset(self):
        return ClientModel.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes =[JWTAuthentication]

    filter_backends=[DjangoFilterBackend]
    filterset_fields =["client", "status"]

    def get_queryset(self):
        user = self.request.user
        queryset= ProjectModel.objects.filter(user=user)
        return queryset
    
    def perform_create(self,serilaizer):
        serilaizer.save(user=self.request.user)


class TodoListView(viewsets.ModelViewSet):
    serializer_class=Todoserializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['project', 'status']

    def get_queryset(self):
        return TodoList.objects.filter(project__user=self.request.user)
    


class UserView(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset = User.objects.all()
    permission_classes=[AllowAny]
    

class customauth(viewsets.ViewSet):
    permission_classes=[AllowAny]
    def create(self, request):
        username= request.data.get('username')
        password = request.data.get('password')
        print(f"DEBUG: Trying to authenticate user - Username: {username}, Password: {password}")
        user = authenticate(username=username, password=password)
        print(f"DEBUG: Authenticated user: {user}")
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({       
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'username':user.username,
                'first_name':user.first_name,
                'email':user.email
            })
        print("DEBUG: Authentication failed")
        return Response({"message":'invalid credentials'}, status=401)