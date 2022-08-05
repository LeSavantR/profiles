from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.views import HelloAPIView, UserProfileViewSet,  UserLogin

router = DefaultRouter()
router.register('profile', UserProfileViewSet, basename='profiles')

appname = 'api'

urlpatterns = [
    path('', HelloAPIView.as_view(), name='hello'),
    path('login/', UserLogin.as_view(), name='login'),
    path('', include(router.urls)),
]