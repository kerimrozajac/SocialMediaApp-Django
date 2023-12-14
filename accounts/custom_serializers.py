# custom_serializers.py
import phonenumbers
import time
import re
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers  # Import the serializers module from Django REST framework

from .models import CustomUser

User = get_user_model()


def validate_phone_number(value):
    """
    Custom validation for the phone number field.
    """
    try:
        parsed_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed_number):
            raise serializers.ValidationError("Invalid mobile number")
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        return formatted_number
    except Exception:
        raise serializers.ValidationError("Invalid mobile number format")


def create_unique_username():
    # Generate a unique username using a timestamp (you can use a different method)
    return f"user_{int(time.time())}"


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(validators=[validate_phone_number], required=True)
    # password2 = serializers.CharField(required=False)
    password2 = None
    username = None
    email = None
    name = None

    def custom_signup(self, request, user):
        user.phone_number = self.validated_data.get('phone_number')
        # user.username = self.generate_unique_username(user.phone_number)
        user.set_password(self.validated_data.get('password'))
        user.save()

    def validate(self, data):
        # Check if a user with the same phone number already exists
        phone_number = data.get("phone_number")
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("User with this phone number already exists.")

        # Create a unique username
        data['username'] = create_unique_username()

        return data


class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

