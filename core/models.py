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
    username = None
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='core/pictures/%Y/%m/%d/', blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    

    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def create_user(self, email, password=None, **extra_fields):
        
        return self._create_user(email, password, **extra_fields)

































'''class Student(models.Model):
    name = models.CharField(max_length=255, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    user_type = models.CharField(max_length=255, default='Student')
    token = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
    total = models.FloatField()
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=255, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=255, default='Teacher')
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    revenue = models.FloatField(default=0)
    show_revenue = models.BooleanField(default=True)

    def __str__(self):
        return self.name

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

    def __str__(self) -> str:
        return self.title

class FlashCard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, default=None, related_name='flashcards')    

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    course_image = models.ImageField(upload_to='core/pictures/%Y/%m/%d')
    teacher_name = models.TextField()
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    course_classification = models.FloatField()
    last_update = models.DateTimeField(auto_now=True)
    course_expiration = models.DateTimeField(auto_now=False, auto_now_add=False)
    #teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Module(models.Model):
    name = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    
class Grade(models.Model):
    name = models.CharField(max_length=255)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    comments = models.TextField()
    video = models.URLField(max_length=255)

class BenefitClub(models.Model):
    benefit_name = models.CharField(max_length=255)
    benefit_description = models.TextField()
    benefit_end_date = models.DateTimeField(auto_now=True)
    benefit_percentage = models.FloatField()
    saved_amount = models.FloatField()
    benefit_link = models.URLField(max_length=255)

class Subscriptions(models.Model):
    #student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subscription_name = models.CharField(max_length=255)
    subscription_description = models.TextField()
    subscription_price = models.FloatField()
    subscription_duration_unit = models.CharField(max_length=50)
    subscription_duration_value = models.IntegerField()
    
class QuestionsMultipeChoice(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    image = models.URLField(max_length=255)
    video = models.URLField(max_length=255)
    type_question = models.CharField(max_length=255)
    right_answer = models.TextField()
    explication = models.TextField()
    alternatives = models.TextField()

class QuestionsText(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    image = models.URLField(max_length=255)
    video = models.URLField(max_length=255)
    type_question = models.CharField(max_length=255)

class Simulated(models.Model):
    #teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    creator = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    limit_time = models.TimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)'''