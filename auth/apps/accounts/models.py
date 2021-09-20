from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=245)
    gender = models.CharField(
        max_length=245, choices=user_gender, default='Male')
    email = models.EmailField(max_length=245, unique=True)
    bio = models.CharField(max_length=101, null=True, blank=True)
    pro_img = models.ImageField(
        upload_to='auth/pro_img', default='auth/pro_img/abstract-user-flat-4.svg')
    token = models.CharField(max_length=245, null=True, blank=True)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.name
