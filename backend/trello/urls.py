from django.urls import path, include
from .views import ProjectViewset, WorkspaceViewset, MyWorkspaceView, TicketViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'workspace', WorkspaceViewset, basename="workspace")
router.register(r'project', ProjectViewset, basename="project")
router.register(r'ticket', TicketViewset, basename="project")
urlpatterns = [
    path('', include(router.urls)),
    path('myworkspace/', MyWorkspaceView.as_view()),
]
