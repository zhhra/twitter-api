from rest_framework.generics import CreateAPIView
from ..serializers.signup_model_serializer import SignUpModelSerializer
from rest_framework.permissions import IsAuthenticated


class Signup(CreateAPIView):
    permission_classes = (~IsAuthenticated,)
    serializer_class = SignUpModelSerializer
