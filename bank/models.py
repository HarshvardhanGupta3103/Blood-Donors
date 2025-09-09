from django.db import models
from django.utils import timezone

class DonorRegistration(models.Model):
    name = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=50, blank=False)
    birth_date = models.DateField(blank=False)  # Date of birth
    blood_group = models.CharField(max_length=10, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=123, blank=False)
    username = models.CharField(max_length=128, unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
    occupation = models.CharField(max_length=100, blank=False)
    home_address = models.CharField(max_length=500, blank=False)
    last_donate_date = models.DateField(blank=True, null=True)  # Can be empty for new donors
    any_disease = models.CharField(max_length=100, blank=True, default="no")
    allergies = models.CharField(max_length=100, blank=True, default="no")
    heart_condition = models.CharField(max_length=100, blank=True, default="no")
    bleeding_disorder = models.CharField(max_length=100, blank=True, default="no")
    hiv_hcv = models.CharField(max_length=50, blank=True, default="no")
    aadhar_card = models.ImageField(upload_to='donor_aadhar/', blank=True, null=True)


    def __str__(self):
        return self.name 

    class Meta:  # Capital "M" here is important
        db_table = "donorList"


class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()
    phone=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name 

    class Meta:  # Capital "M" here is important
        db_table = "contact_us"

