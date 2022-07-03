from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, Project, Ticket
from rest_framework import viewsets, mixins, status, permissions
from .models import Workspace
from .serializers import ProjectSerializer, TicketSerializer, WorkspaceSerializer
# Create your views here.


class WorkspaceViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data["owner_id"] = request.user.id
        data["users"] = [request.user.id]
        data["projects"] = []
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MyWorkspaceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        workspaces = request.user.workspace_set.all()
        serializer = WorkspaceSerializer(workspaces, many=True)
        return Response(serializer.data)


class ProjectViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TicketViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
