from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    username = None
    email = models.EmailField(unique=True)
    objects = UserManager()
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


class Category(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Deck(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_flashcards(self):
        flashcards = FlashCard.objects.filter(deck=self)
        return flashcards

    def __str__(self) -> str:
        return self.title

class FlashCard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, default=None, related_name='flashcards')    