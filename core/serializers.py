from rest_framework import serializers

from . import models



class StudentAddPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['name', 'points']

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