from rest_framework import serializers
from app.models import Recipient


class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient
        fields = '__all__'
