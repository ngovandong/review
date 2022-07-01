from django.contrib import admin
from django.urls import path, include
from .views import MyView, SignUpViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'signup', SignUpViewSet, basename="signup")
urlpatterns = [
    path('', include(router.urls)),
    path('my/', MyView.as_view(), name='signup'),
]