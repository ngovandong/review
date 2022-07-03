from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PowerUserSerializer, UserSerializer
from .models import CustomUser
from rest_framework import viewsets, mixins, status, permissions
from .permissions import AdminPermission
from rest_framework.decorators import action
# Create your views here.


class MyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class NormalUserViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, AdminPermission]
    queryset = CustomUser.objects.all()
    serializer_class = PowerUserSerializer

    @action(detail=False, methods=["GET"])
    def power_user(self, request):
        qs = CustomUser.objects.filter(role="PU")
        if qs.exists():
            serializer = UserSerializer(qs, many=True)
            return Response(serializer.data)
        return Response([])

    @action(detail=False, methods=["GET"])
    def normal_user(self, request):
        qs = CustomUser.objects.filter(role="NU")
        if qs.exists():
            serializer = UserSerializer(qs, many=True)
            return Response(serializer.data)
        return Response([])
