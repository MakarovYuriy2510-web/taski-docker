"""DockSTRING."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """DockSTRING."""

    class Meta:
        """DockSTRING."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
