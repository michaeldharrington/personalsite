from rest_framework import serializers
from public.models import Project, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'full_text', 'img', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
