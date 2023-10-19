# custom_views.py
from dj_rest_auth.registration.views import RegisterView
from .custom_serializers import CustomRegisterSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
