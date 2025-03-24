from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClientModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone= models.CharField(max_length=20, unique=True ,null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class ProjectModel(models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('InProgress', 'InProgress'),
        ('Done', "Done")
    )
    name=models.CharField(max_length=100)
    description=models.TextField()
    deadline=models.DateField()
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    client = models.ForeignKey(ClientModel, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " - " +str(self.client)
    

class TodoList(models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('Inprogress', 'Inprogress'),
        ('Done', 'Done')
    )
    task = models.CharField(max_length=128, null=True)
    created_at = models.DateField(auto_now_add=True)
    target_time =models.DateField()
    status = models.CharField(max_length=20, null=True, choices=STATUS)

    project = models.ForeignKey(ProjectModel, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.task) + " - " + str(self.project)