from rest_framework import serializers
from todo.models import TodoTaskModel


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTaskModel
        fields = '__all__'


class TodoTaskCompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTaskModel
        fields = ['completed']

class TodoTaskRescheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTaskModel
        fields = ['scheduled_at']