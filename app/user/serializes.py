"""Serializes for the user API View"""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'field']
        extra_kwargs = {'password' : {'write_only': True, 'min_length': 5}}

    def create(self, validates_data):
        """Create user and return user with encrypted password"""
        return get_user_model().objects.create_user(**validates_data)


