from rest_framework import serializers

from . import models


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
        
    
    