from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from app.models import Task
from app.serializers.task_serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

