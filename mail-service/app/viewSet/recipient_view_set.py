from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from app.models import Recipient
from app.serializers.recipient_serializer import RecipientSerializer

class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    permission_classes = [AllowAny]