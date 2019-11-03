from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50),
    maintext = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)


class Signup(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    


