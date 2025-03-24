from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientView, basename='client')
router.register(r'projects', ProjectView, basename='project')
router.register(r'todo', TodoListView, basename='todo')
router.register(r'users', UserView, basename='user')
router.register(r'auth', customauth, basename='auth')

urlpatterns = [
    path('api/', include(router.urls)),
   
    # path('home/', simpleview, name='simpleview')
]
