from rest_framework import serializers
from ..models.user import User
from accounts.tasks.send_activation_email import send_activation_email
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class SignUpModelSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "birth_date",
            "sex",
            "phone_number",
            "password",
            "password2",
        ]

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists() and value:
            raise serializers.ValidationError("the number already exists")
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password fields didn't match.")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create(**validated_data, is_active=False)
        user.set_password(validated_data["password"])
        user.save()
        send_activation_email.delay(user.username, user.email)
        return user
