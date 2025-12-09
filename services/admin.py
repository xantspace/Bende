from django.contrib import admin
from .models import Birth_certificate

# Register your models here.
@admin.register(Birth_certificate)
class BirthCertAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'gender', 'father_name', 'phone', 'home_address')
    search_fields = ('first_name', 'surname', 'father_name', 'phone', 'home_address')
    list_filter = ('gender',)