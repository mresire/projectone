from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['name','is_completed']