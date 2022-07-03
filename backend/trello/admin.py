from django.contrib import admin
from .models import Comment, Workspace, Project, Ticket
admin.site.register(Comment)
admin.site.register(Workspace)
admin.site.register(Project)
admin.site.register(Ticket)
