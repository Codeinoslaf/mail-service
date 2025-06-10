from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app.models import Status
from app.serializers.status_serializer import StatusSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]