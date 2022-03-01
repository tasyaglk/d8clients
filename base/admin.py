from django.contrib import admin
from .models import User, Client, Employee, Organization


admin.site.register(User)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Organization)
