from django.urls import path, include
from .views import MyView, NormalUserViewset, AdminViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'normal', NormalUserViewset, basename="normal")
router.register(r'power', AdminViewSet, basename="power")
urlpatterns = [
    path('', include(router.urls)),
    path('my/', MyView.as_view(), name='signup'),
]
