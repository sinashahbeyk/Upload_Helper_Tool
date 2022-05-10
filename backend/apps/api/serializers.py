from rest_framework import serializers
from django.contrib.auth.models import User
from apps.blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        # fields = ["title", "author", "create_at", "status"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username", "email", "first_name", "last_name"]
