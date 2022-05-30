from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todolist.models import Task
from todolist.serializers import TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """View to manipulate Users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Views to manipulate Tasks."""

    queryset = Task.objects.select_related("owner").all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
