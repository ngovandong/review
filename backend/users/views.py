from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework import  viewsets, mixins, status, permissions

# Create your views here.
class MyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)


class SignUpViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
