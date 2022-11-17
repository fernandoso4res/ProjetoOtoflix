from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from . import models, serializers


class StudentAPIv1ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()


class FlashCardAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FlashCardSerializer
    queryset = models.FlashCard.objects.all()


class DeckAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeckSerializer
    queryset = models.Deck.objects.all()
    