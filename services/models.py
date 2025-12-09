from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Birth_certificate(models.Model):
    # child's information
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    dob = models.DateField()
    GENDER_CHOICES = {
        'male': 'Male',
        'female': 'Female'
    }
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    place_of_birth = models.CharField(max_length=100, blank=True)

    # parents information
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(
        max_length=15, blank=True)
    home_address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

    class Meta:
        verbose_name = "Birth Certificate"
        verbose_name_plural = "Birth Certificates"


class Marriage_certificate(models.Model):
    MARRIAGE_CHOICES = {
        'statutory_marriage': 'Statutory Marriage',
        'customary_marriage': 'Customary Marriage',
        'renewal_of_vows': 'Renewal Of Vows',
    }
    marriage_type = models.CharField(max_length=30, choices=MARRIAGE_CHOICES)
    # grooms details
    groom_full_name = models.CharField(max_length=40)
    groom_dob = models.DateField()
    MARITAL_CHOICES = {
        'single': 'Single',
        'divorced': 'Divorced',
        'widowed': 'Widowed',
    }
    marital_status = models.CharField(max_length=15, choices=MARITAL_CHOICES)
    groom_occupation = models.CharField(max_length=50)
    groom_residence = models.CharField(max_length=100)

    # brides details
    bride_full_name = models.CharField(max_length=40)
    bride_deb = models.DateField()
    bride_marital_status = models.CharField(
        max_length=15, choices=MARITAL_CHOICES)
    bride_occupation = models.CharField(max_length=50)
    bride_residence = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.groom_full_name} - {self.bride_full_name}"


