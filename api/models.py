from django.db import models

# Create your models here.

class Insurance(models.Model):
        class InsuranceType(models.TextChoices):
                
            LIFE = 'life', 'Life Insurance'
            HEALTH = 'health', 'Health Insurance'
            VEHICLE = 'vehicle', 'Vehicle Insurance'
            PROPERTY = 'property', 'Property Insurance'

        customer=models.CharField(max_length=100)
        contact=models.CharField(max_length=10)
        address=models.CharField(max_length=100)
        insurance_type=models.CharField(max_length=100,choices=InsuranceType.choices)
