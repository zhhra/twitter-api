from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    SEX_CHOICES = [
        ("m", "male"),
        ("f", "female"),
        ("o", "others"),
    ]
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    followings = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )

    def followings_count(self):
        return self.followings.count()

    def followers_count(self):
        return self.followers.count()
