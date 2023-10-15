# custom_serializers.py
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers  # Import the serializers module from Django REST framework
import phonenumbers


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(required=True)
    password2 = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match")

        # Implement any other custom validation logic here

        return data

    def validate_mobile_number(self, value):
        try:
            parsed_number = phonenumbers.parse(value, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise serializers.ValidationError("Invalid mobile number")
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            return formatted_number
        except Exception:
            raise serializers.ValidationError("Invalid mobile number format")