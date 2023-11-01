# custom_views.py
from dj_rest_auth.registration.views import RegisterView
from .custom_serializers import CustomRegisterSerializer, CustomLoginSerializer
from dj_rest_auth.views import LoginView


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


class CustomLoginView(LoginView):
    #authentication_classes = ['app_name.backends.PhoneBackend', ]
    serializer_class = CustomLoginSerializer
