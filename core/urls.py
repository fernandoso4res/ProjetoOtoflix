from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)

from . import views

router = routers.SimpleRouter()
router.register(r'student', views.StudentAPIv1ViewSet)
router.register(r'flashcards', views.FlashCardAPIv1ViewSet)
router.register(r'decks', views.DeckAPIv1ViewSet)
router.register(r'subscriptions', views.SubscriptionsAPIv1ViewSet)
router.register(r'questions-multiple-choice', views.QuestionsMultipleChoiceAPIv1ViewSet)
router.register(r'questions-text', views.QuestionsTextAPIv1ViewSet)
router.register(r'simulated', views.SimulatedAPIv1ViewSet)
router.register(r'user', views.UserAPIv1ViewSet)
router.register(r'student-add-points', views.StudentAddPointAPIv1ViewSet)

urlpatterns = [
    path('api/v1/', include((router.urls, 'core'))),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/', include((router.urls, 'core'))),
]
