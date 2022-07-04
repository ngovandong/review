from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PowerUserSerializer, UserSerializer
from .models import CustomUser
from rest_framework import viewsets, mixins, status, permissions
from .permissions import PowerUserOrAdminPermission
from rest_framework.decorators import action
from trello.models import Workspace
from django.shortcuts import get_object_or_404


# Create your views here.


class MyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class NormalUserViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, PowerUserOrAdminPermission]
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


    @action(detail=False, methods=["GET"], name='workspace_user')
    def workspace_user(self, request):
        id = request.query_params.get('id')

        try:
            w = Workspace.objects.get(pk=id)
            serializer = UserSerializer(instance=w.users, many=True)
            return Response(serializer.data)
        except Workspace.DoesNotExist:
            return Response(status=400)

    @action(detail=False, methods=["GET"], name='search_user')
    def search_user(self, request):
        email = request.query_params.get('email')
        user=get_object_or_404(CustomUser, email=email)
        serializer=UserSerializer(user)
        return Response(serializer.data)
