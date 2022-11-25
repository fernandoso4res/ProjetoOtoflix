from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from .permis import IsStudent

from . import models, serializers




class UserAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    http_method_names = ['get', 'patch', 'delete']

class StudentAPIv1Create(CreateAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = models.User.objects.all()

class AdministratorAPIv1Create(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


'''class StudentAPIv1ViewSet(viewsets.ModelViewSet):
    permissions_classes = [IsStudent, ]
    serializer_class = serializers.StudentSerializer
    queryset = models.User.objects.all()
    http_method_names = ['get', 'patch', 'delete']'''

































'''class TeacherAPIv1Create(CreateAPIView):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teacher.objects.all()




class SimulatedAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SimulatedSerializer
    queryset = models.Simulated.objects.all()


class QuestionsTextAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionsTextSerializer
    queryset = models.QuestionsText.objects.all()

class QuestionsMultipleChoiceAPIv1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionsMultipleChoiceSerializer
    queryset = models.QuestionsMultipeChoice.objects.all()


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
'''
