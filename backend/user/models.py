from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Profile(User):
    username_lowercase = models.CharField(max_length=255, unique=True)
    followers = models.ManyToManyField('self', blank=True)
    following = models.ManyToManyField('self', blank=True)
    class Meta:
        db_table = 'Profile'


class Admin(Profile):
    class Meta:
        db_table = 'Admin'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)