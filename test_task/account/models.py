from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.URLField(default='https://live.staticflickr.com/5252/5403292396_0804de9bcf_b.jpg')
