from django.urls import include, path
from rest_framework import routers
<<<<<<< HEAD
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)
=======
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
>>>>>>> 224526c90154da97a30a4cd438c928f2ebf3717d

from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



router = routers.SimpleRouter()
router.register(r'flashcards', views.FlashCardAPIv1ViewSet)
router.register(r'decks', views.DeckAPIv1ViewSet)
<<<<<<< HEAD
router.register(r'subscriptions', views.SubscriptionsAPIv1ViewSet)
router.register(r'questions-multiple-choice', views.QuestionsMultipleChoiceAPIv1ViewSet)
router.register(r'questions-text', views.QuestionsTextAPIv1ViewSet)
router.register(r'simulated', views.SimulatedAPIv1ViewSet)
router.register(r'user', views.UserAPIv1ViewSet)
router.register(r'student-add-points', views.StudentAPIv1ViewSet)
=======
>>>>>>> 224526c90154da97a30a4cd438c928f2ebf3717d
router.register(r'benefits_club', views.BenefitClubAPIv1ViewSet)
router.register(r'subscriptions', views.SubscriptionsAPIv1ViewSet)
router.register(r'users', views.UserAPIv1ViewSet)
router.register(r'students', views.StudentAPIv1ViewSet)
router.register(r'questions-multiple-choice', views.QuestionsMultipleChoiceAPIv1ViewSet)
router.register(r'questions-text', views.QuestionsTextAPIv1ViewSet)
router.register(r'simulated', views.SimulatedAPIv1ViewSet)

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/auth/register-student/', views.StudentAPIv1Create.as_view(), name='register-student'),
    path('api/v1/auth/register-teacher/', views.TeacherAPIv1Create.as_view(), name='register-teacher'),
    path('api/v1/auth/register-administrator/', views.AdministratorAPIv1Create.as_view(), name='register-administrator'),
<<<<<<< HEAD
    path('api/v1/', include((router.urls, 'core'))),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
=======
>>>>>>> 224526c90154da97a30a4cd438c928f2ebf3717d
    path('api/v1/', include((router.urls, 'core'))),

    path('ap1/v1/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
