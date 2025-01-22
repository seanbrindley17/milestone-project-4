from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# View for a user's profile and default information
class UserProfile(models.Model):
    # OneToOneField specifies that user can only have one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    town_or_city = models.CharField(max_length=30, null=True, blank=True)
    address_line_one = models.CharField(max_length=50, null=True, blank=True)
    address_line_two = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=30, null=True, blank=True)
