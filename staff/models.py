from django.db import models
from base.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='employees')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='admins')
    is_host = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)