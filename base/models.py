from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    ROLE = [
        ('client', 'client'),
        ('employee', 'employee')
    ]
    type = models.CharField(max_length=100, choices=ROLE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Organization(models.Model):
    name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return str(self.user.username)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, related_name='employees')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)