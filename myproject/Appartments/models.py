from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class AmenityModel(models.Model):
    name = models.CharField(max_length=255)

# Choices for location zoning
LOCATION_CHOICES = [
    ('commercial', 'Commercial'),
    ('residential', 'Residential'),
]

# Choices for booking status
STATUS_CHOICES = [
    ('booked', 'Booked'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed'),
]

class ApartmentModel(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    amenities = models.ManyToManyField(AmenityModel)
    booked = models.BooleanField(default=False)
    photo_url = models.URLField(blank=True, null=True)

class LandModel(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    price_per_acre = models.DecimalField(max_digits=10, decimal_places=2)
    zoning = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    photo_url = models.URLField(blank=True, null=True)

class AirbnbModel(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    amenities = models.ManyToManyField(AmenityModel)
    max_guests = models.PositiveIntegerField(default=1)
    booked = models.BooleanField(default=False)
    photo_url = models.URLField(blank=True, null=True)

class MaintenanceRequestModel(models.Model):
    apartment = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE)
    issue_description = models.TextField()
    solved = models.BooleanField(default=False)

class InquiryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #land = models.ForeignKey(LandModel, on_delete=models.CASCADE)
    message = models.TextField()
    solved = models.BooleanField(default=False)

class AppartmentBookingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)

class AirbnbBookingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    airbnb = models.ForeignKey(AirbnbModel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booked = models.BooleanField(default=False)

class CleanerModel(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    photo_url = models.URLField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

class TransportServiceModel(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    photo_url = models.URLField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

class CommunityForumPostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
