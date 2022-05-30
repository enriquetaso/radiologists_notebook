from django.contrib.auth.models import User
from rest_framework import serializers
from todolist.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "created", "title", "description", "done", "owner"]
        read_only_fields = ["owner"]

    def create(self, validated_data):
        owner = self.context["request"].user
        return Task.objects.create(owner=owner, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
