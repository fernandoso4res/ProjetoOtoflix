from rest_framework import serializers

from . import models


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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_student', 'is_teacher', 'profile_picture']


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriptions
        fields = ['id', 'student_id', 'subscription_name', 'subscription_description', 'subscription_price', 'subscription_duration_unit', 'subscription_duration_value', ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'user', 'user_type', 'created_at', 'total']