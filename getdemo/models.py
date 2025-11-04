from django.db import models


# basic model for db integration
# Table 1
class Yard(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
     return self.name

# Table 2
class Coil(models.Model):
    # coil_name : attrtibute of the coil
    
    # models.CharField → Field type in Django ORM, represents a short string/text column.
    
    #max_length=100 → Maximum allowed characters in this field.
    coil_name = models.CharField(max_length=100)
    weight = models.FloatField()  # in tons
    status = models.CharField(max_length=50, default="Available")  # Available / Dispatched
    # foreign Key -> link to Yard Model
    yard = models.ForeignKey(Yard, on_delete=models.CASCADE, related_name="coils")
    
    def __str__(self):
        return f"{self.coil_name} ({self.yard.name})"

# When you migrate, Django creates a column like:
# coil_name VARCHAR(100) NOT NULL

# Understanding:
# yard_location = models.CharField(max_length=100)
# weight = models.FloatField()
# status = models.CharField(max_length=50, default="Available")

# map to DB fields like:
# yard_location VARCHAR(100) NOT NULL,
# weight FLOAT NOT NULL,
# status VARCHAR(50) DEFAULT 'Available'

# __str__ → Controls the string representation of objects (for humans).
# models.CharField(...) → Defines a string-type database column with validation (max length).