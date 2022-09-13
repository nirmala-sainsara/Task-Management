from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =Task
        fields = ['is_marked_completed_task']

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Task
        fields = ['task_name', 'end_date']

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =Task
        fields = ['id', 'user', 'task_name', 'task_description', 'start_date', 'end_date', 'is_marked_completed_task']

        read_only_fields = ('id',)

