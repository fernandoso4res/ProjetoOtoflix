from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models


'''class UserAdmin(BaseUserAdmin):
    
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_staff', 'is_student')}),
        
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_student'),
        }),
    )
    ordering = ('email',)'''
    



admin.site.register(models.User)


















'''
#admin.site.register(models.Student)
#admin.site.register(models.Teacher)
admin.site.register(models.FlashCard)
admin.site.register(models.Category)
admin.site.register(models.Deck)
admin.site.register(models.Course)
admin.site.register(models.Module)
admin.site.register(models.BenefitClub)
admin.site.register(models.Subscriptions)
admin.site.register(models.QuestionsMultipeChoice)
admin.site.register(models.QuestionsText)
admin.site.register(models.Simulated)'''