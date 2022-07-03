from rest_framework import serializers
from .models import Comment, CustomUser, Project, Ticket, Workspace


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'name', 'status', 'desc', 'project']


class ProjectSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'workspace', 'tickets']


class WorkspaceSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'users', 'projects', 'owner_id']
