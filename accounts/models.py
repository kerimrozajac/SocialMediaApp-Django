from django.contrib.auth.models import AbstractUser
from django.db import models
import phonenumbers


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def clean_phone_number(self):
        try:
            parsed_number = phonenumbers.parse(self.phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError('Invalid phone number')
            return self.phone_number
        except phonenumbers.phonenumberutil.NumberFormatError:
            raise ValidationError('Invalid phone number')
