from django.db import models

# Create your models here.
class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('driver', 'Driver'),
    )

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email
    
class Taxi(models.Model):
    CAR_TYPE_CHOICES = (
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('van', 'Van'),
        # Add more choices as needed
    )

    driver = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    location = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.driver.full_name}'s {self.get_car_type_display()} - {self.location}"