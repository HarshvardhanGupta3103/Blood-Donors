from django.contrib import admin
from .models import DonorRegistration

@admin.register(DonorRegistration)
class DonorRegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'blood_group', 'phone_number', 'email', 'birth_date', 'last_donate_date']
    list_filter = ['blood_group', 'gender', 'any_disease', 'allergies']
    search_fields = ['name', 'phone_number', 'email', 'username']
    readonly_fields = ['username']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'username', 'gender', 'birth_date', 'phone_number', 'email', 'occupation', 'home_address')
        }),
        ('Blood Information', {
            'fields': ('blood_group', 'last_donate_date')
        }),
        ('Medical Information', {
            'fields': ('any_disease', 'allergies', 'heart_condition', 'bleeding_disorder', 'hiv_hcv')
        }),
        ('Documents', {
            'fields': ('aadhar_card',)
        }),
    )  