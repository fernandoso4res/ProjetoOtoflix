from django.contrib import admin

from core import models

admin.site.register(models.User)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.FlashCard)
admin.site.register(models.Category)
admin.site.register(models.Deck)
