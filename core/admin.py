from django.contrib import admin
from core import models

admin.site.register(models.User)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
