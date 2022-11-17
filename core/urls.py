from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'student', views.StudentAPIv1ViewSet)
router.register(r'flashcards', views.FlashCardAPIv1ViewSet)
router.register(r'decks', views.DeckAPIv1ViewSet)


urlpatterns = [
    path('api/v1/', include((router.urls, 'core'))),
]
