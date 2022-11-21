from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['is_student', 'is_teacher', 'username', 'email']

class SimulatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Simulated
        fields = ['teacher_id', 'creator', 'created_at', 'limit_time', 'category']

class QuestionsTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionsText
        fields = ['category', 'question', 'image', 'video', 'type_question']

class QuestionsMultipleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionsMultipeChoice
        fields = ['category', 'question', 'image', 'video', 'type_question', 'right_answer', 'explication', 'alternatives']

class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriptions
        fields = ['subscriptions_id', 'subscriptions_name', 'subscriptions_description', 'subscriptions_price', 'subscriptions_duration_unit', 'subscriptions_duration_value']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'name', 'nickname', 'lastname', 'proflie_picture']
        

class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlashCard
        fields = ['id', 'question', 'answer', 'category', 'deck']
    

    category = serializers.StringRelatedField(many=False)

class DeckSerializer(serializers.ModelSerializer):
    flashcards = FlashCardSerializer(many=True, read_only=True)
    class Meta:
        model = models.Deck
        fields = ['id', 'title', 'user', 'flashcards']
        
    
class BenefitsClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BenefitClub
        fields = ['id', 'benefit_name', 'benefit_description', 'benefit_end_date', 'benefit_percentage', 'saved_amount', 'benefit_link']

class QuestionsTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionsText
        fields = ['category', 'question', 'image', 'video', 'type_question']
        
class QuestionsMultipleChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionsMultipeChoice
        fields = ['category', 'question', 'image', 'video', 'type_question', 'right_answer', 'explication', 'alternatives']


class BaseUserRegisterMixin:
    def create_user(self, validated_data, is_student=False, is_teacher=False) -> models.User:
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        nickname = validated_data['nickname']
        password = validated_data['password']
        user = models.User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            nickname=nickname,
            password=password,
            is_student=is_student,
            is_teacher=is_teacher,
        )
        user.set_password(password)
        user.save()
        return user
    
    def validate_email(self, value):
        email_exists = models.User.objects.filter(email=value).exists()

        if email_exists:
            raise ValidationError('Erro, email cadastrado já existe!')

        return value

class UserSerializer(serializers.ModelSerializer, BaseUserRegisterMixin):
    password = serializers.CharField(max_length=150, write_only=True)
    class Meta:
        model = models.User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_student', 'is_teacher', 'password', 'nickname' , 'profile_picture']
    
    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        nickname = validated_data['nickname']
        password = validated_data['password']
        user = models.User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            nickname=nickname,
            password=password,
            is_staff=True,
        )
        user.set_password(password)
        user.save()
        return user


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriptions
        fields = ['id', 'student_id', 'subscription_name', 'subscription_description', 'subscription_price', 'subscription_duration_unit', 'subscription_duration_value', ]


class StudentSerializer(serializers.ModelSerializer, BaseUserRegisterMixin):
    first_name = serializers.CharField(max_length = 150, write_only=True)
    last_name = serializers.CharField(max_length = 150, write_only=True)
    email = serializers.EmailField(write_only=True)
    nickname = serializers.CharField(max_length = 255, write_only=True)
    password = serializers.CharField(max_length = 255, write_only=True)

    class Meta:
        model = models.Student
        fields = ['id', 'user', 'user_type', 'created_at', 'total', 'first_name', 'last_name', 'email', 'nickname', 'password']
        read_only_fields = ['id', 'user', 'user_type', 'created_at', 'total']
    

    def create(self, validated_data):
        user = self.create_user(validated_data, is_student=True)
        student = models.Student.objects.create(user=user, total=0)
        return student


class TeacherSerializer(serializers.ModelSerializer, BaseUserRegisterMixin):
    first_name = serializers.CharField(max_length = 150, write_only=True)
    last_name = serializers.CharField(max_length = 150, write_only=True)
    email = serializers.EmailField(write_only=True)
    nickname = serializers.CharField(max_length = 255, write_only=True)
    password = serializers.CharField(max_length = 255, write_only=True)

    class Meta:
        model = models.Teacher
        fields = ['id', 'user', 'user_type', 'token', 'created_at', 'revenue','show_revenue', 'first_name', 'last_name', 'email', 'nickname', 'password']
        read_only_fields = ['id', 'user', 'user_type', 'created_at', 'token', ]
    
    def create(self, validated_data):
        user = self.create_user(validated_data, is_student=False, is_teacher=True)
        teacher = models.Teacher.objects.create(user=user, revenue=0, show_revenue=True)
        return teacher


class SimulatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Simulated
        fields = ['teacher_id', 'creator', 'created_at', 'limit_time', 'category']
