from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from . import models, serializers


class FlashCardAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FlashCardSerializer
    queryset = models.FlashCard.objects.all()


class DeckAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DeckSerializer
    queryset = models.Deck.objects.all()


class BenefitClubAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BenefitsClubSerializer
    queryset = models.BenefitClub.objects.all()


class SubscriptionsAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SubscriptionsSerializer
    queryset = models.Subscriptions.objects.all()


class UserAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    http_method_names = ['get', 'patch', 'delete']


class StudentAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
    http_method_names = ['get', 'patch', 'delete']


class StudentAPIv1Create(CreateAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()


class TeacherAPIv1Create(CreateAPIView):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teacher.objects.all()

class AdministratorAPIv1Create(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()