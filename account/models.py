from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
from account.manager import UserManager


class User(AbstractUser):
    username = None
    email = None
    # name = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^998\d{9}$', message="Telefon raqam +9981234567 formatida bo'lishi kerak")
    phone_number = models.CharField(
        max_length=12, unique=True, validators=[phone_regex])
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, default="")
    count = models.IntegerField(default=0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
