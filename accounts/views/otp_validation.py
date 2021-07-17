from rest_framework.permissions import IsAuthenticated
from ..serializers.otp_validation_model_serializer import OtpValidationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from ..models.user import User


class OtpValidation(APIView):
    permission_classes = (~IsAuthenticated,)
    serializer_class = OtpValidationSerializer

    def post(self, request, format=None):
        entered_password = request.data.get("entered_password")
        if entered_password in cache:
            username = cache.get(entered_password)
            user = User.objects.filter(username=username, is_active=False).first()
            if user:
                user.is_active = True
                user.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)
