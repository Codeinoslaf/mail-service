from rest_framework import serializers
from app.models import Email
from .recipient_serializer import RecipientSerializer
from .status_serializer import StatusSerializer
from .task_serializer import TaskSerializer


class EmailSerializer(serializers.ModelSerializer):
    send_at = serializers.SerializerMethodField()
    status = StatusSerializer()
    task = TaskSerializer()
    recipient_list = RecipientSerializer(many=True)

    def get_send_at(self, obj):
        return int(obj.send_at.timestamp() * 1000) if obj.send_at else None

    class Meta:
        model = Email
        fields = '__all__'
