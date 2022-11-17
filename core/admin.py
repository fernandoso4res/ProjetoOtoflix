from django.contrib import admin

from core import models

admin.site.register(models.User)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.FlashCard)
admin.site.register(models.Category)
admin.site.register(models.Deck)
admin.site.register(models.Course)
admin.site.register(models.Module)
admin.site.register(models.BenefitClub)
admin.site.register(models.Subscriptions)
admin.site.register(models.QuestionsMultipeChoice)
admin.site.register(models.QuestionsText)
admin.site.register(models.Simulated)