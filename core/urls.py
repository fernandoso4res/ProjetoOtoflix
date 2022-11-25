from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from . import views

router = routers.SimpleRouter()
'''
router.register(r'flashcards', views.FlashCardAPIv1ViewSet)
router.register(r'decks', views.DeckAPIv1ViewSet)
router.register(r'benefits_club', views.BenefitClubAPIv1ViewSet)
router.register(r'subscriptions', views.SubscriptionsAPIv1ViewSet)
router.register(r'users', views.UserAPIv1ViewSet)'''



#router.register(r'students', views.StudentAPIv1Create.as_view())


'''
router.register(r'questions-multiple-choice', views.QuestionsMultipleChoiceAPIv1ViewSet)
router.register(r'questions-text', views.QuestionsTextAPIv1ViewSet)
router.register(r'simulated', views.SimulatedAPIv1ViewSet)
'''

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/auth/register-student/', views.StudentAPIv1Create.as_view(), name='register-student'),
    #path('api/v1/auth/register-teacher/', views.TeacherAPIv1Create.as_view(), name='register-teacher'),
    path('api/v1/auth/register-administrator/', views.AdministratorAPIv1Create.as_view(), name='register-administrator'),
    path('api/v1/', include((router.urls, 'core'))),
]
