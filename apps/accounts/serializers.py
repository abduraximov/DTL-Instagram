from rest_framework import serializers
from django.contrib.auth.models import User
from apps.profiles.models import Profile
from rest_framework.validators import UniqueValidator


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=255,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='This email address is already in use.')
        ],
        style={'input_type': 'email', 'placeholder': 'Email'}
    )
    username = serializers.CharField(
        max_length=255,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='This username is already in use.')
        ],
        style={'input_type': 'text', 'placeholder': 'Username'},
    )
    password = serializers.CharField(
        max_length=255,
        required=True,
        min_length=8,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    full_name = serializers.CharField(
        max_length=64,
        required=True,
        min_length=4,
        style={'input_type': 'text', 'placeholder': 'Full name'}
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'full_name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user, full_name=validated_data['full_name'])
        return validated_data