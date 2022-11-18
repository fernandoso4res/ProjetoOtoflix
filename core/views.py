from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from . import models, serializers

class StudentAddPointAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentAddPointSerializer
    queryset = models.Student.objects.all()

class UserAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class SimulatedAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SimulatedSerializer
    queryset = models.Simulated.objects.all()

class QuestionsTextAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionsTextSerializer
    queryset = models.QuestionsText.objects.all()

class QuestionsMultipleChoiceAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionsMultipleChoiceSerializer
    queryset = models.QuestionsMultipeChoice.objects.all()

class SubscriptionsAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SubscriptionsSerializer
    queryset = models.Subscriptions.objects.all()

class StudentAPIv1ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()


class FlashCardAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FlashCardSerializer
    queryset = models.FlashCard.objects.all()


class DeckAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeckSerializer
    queryset = models.Deck.objects.all()
    
