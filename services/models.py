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