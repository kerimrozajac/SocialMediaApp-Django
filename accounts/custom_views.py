# custom_views.py
from dj_rest_auth.registration.views import RegisterView
from .custom_serializers import CustomRegisterSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


    # def create(self, request, *args, **kwargs):
    #     # If 'password2' is not present in the request, set it to the same value as 'password'
    #     if 'password2' not in request.data:
    #         request.data['password2'] = request.data['password1']
    #
    #     return super(CustomRegisterView, self).create(request, *args, **kwargs)
