from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(TodoList)
admin.site.register(ClientModel)