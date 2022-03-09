from django.db import models
from base.models import User
# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client', null=False)

    def __str__(self):
        return self.user.get_full_name()