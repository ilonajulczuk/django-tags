from rest_framework import serializers

from .models import Library, Tag


class TagSerializer(serializers.ModelSerializer):
    libraries = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Tag


class LibrarySerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='text'
    )

    class Meta:
        model = Library
