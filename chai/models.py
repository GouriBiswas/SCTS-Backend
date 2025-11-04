from django.db import models
from django.utils import timezone

# Create your models here.
class Coil(models.Model):
    STATUS_CHOICES = [
        ("AVAILABLE", "Available"),
        ("DISPATCHED", "Dispatched"),
        ("SCRAP", "Scrap"),
    ]
    
    coil_id = models.CharField(max_length=50, unique=True)
    material = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)  # in kg
    yard_location = models.CharField(max_length=20)
    received_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="AVAILABLE")
    
    def __str__(self):
        return f"{self.coil_id} ({self.material})"


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.car_name} ({self.speed} km/h)"


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']
        
        


# Model structure:- 
# class Student(models.Model):
#     # id = models.AutoField() --> primary field jo django khud add krta hai
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField()
#     address = models.TextField()
#     image = models.ImageField()
#     file = models.FileField()
    
    
#     class Product(models.Model):
#         pass


