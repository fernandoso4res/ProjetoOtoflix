from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Courses(models.Model):
    ...

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    proflie_picture = models.ImageField(upload_to='core/pictures/%Y/%m/%d/')
    user_type = models.CharField(max_length=255)
    token = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
    total = models.FloatField()
     
    
    
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='core/pictures/%Y/%m/%d/')
    user_type = models.CharField(max_length=255)
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    revenue = models.FloatField()
    show_revenue = models.BooleanField()