from rest_framework import serializers


class OtpValidationSerializer(serializers.Serializer):
    entered_password = serializers.CharField(write_only=True, required=True)
