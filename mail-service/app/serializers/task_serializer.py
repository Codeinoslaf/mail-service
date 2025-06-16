from rest_framework import serializers
from app.models import Task, Email



class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()


    def get_created_at(self, obj):
        return int(obj.created_at.timestamp() * 1000) if obj.created_at else None

    class Meta:
        model = Task
        fields = '__all__'