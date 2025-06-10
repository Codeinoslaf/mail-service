from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from app.models import Email
from app.serializers.email_serializer import EmailSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]