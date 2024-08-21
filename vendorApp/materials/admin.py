from django.contrib import admin
from .models import Role, CustomUser, Material, Vehicle

admin.site.register(Role)
admin.site.register(CustomUser)
admin.site.register(Material)
admin.site.register(Vehicle)