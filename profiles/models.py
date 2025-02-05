from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# View for a user's profile and default information
class UserProfile(models.Model):
    # OneToOneField specifies that user can only have one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    surname = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    town_or_city = models.CharField(max_length=30, null=True, blank=True)
    address_line_one = models.CharField(max_length=50, null=True, blank=True)
    address_line_two = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.username


# Signal for post_save event so that profile is either created
# or updated when user object is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save(
        update_fields=["name", "surname", "phone_number", "email"]
    )
