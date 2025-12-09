from django.contrib import admin
from .models import Birth_certificate, Marriage_certificate


# Register your models here.


@admin.register(Birth_certificate)
class BirthCertAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'gender',
                    'father_name', 'phone', 'home_address')
    search_fields = ('first_name', 'surname',
                     'father_name', 'phone', 'home_address')
    list_filter = ('gender',)


@admin.register(Marriage_certificate)
class MarriageCertAdmin(admin.ModelAdmin):
    list_display = ('marriage_type', 'groom_full_name',
                    'bride_full_name', 'bride_deb')
    search_fields = ('marriage_type', 'full_name', 'bride_full_name')
    list_filter = ('marriage_type',)
