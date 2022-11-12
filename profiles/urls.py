from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.views import UserLogout, UserProfileViewSet,  UserLogin
from app.views import InvoiceViewSet, ItemViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet, basename='profiles')
router.register('invoice', InvoiceViewSet, basename='invoices')
router.register('item', ItemViewSet, basename='items')

appname = 'api'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('v1/', include(router.urls)),
]