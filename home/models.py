from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    subcategories = models.ManyToManyField("SubCategory", blank=True)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(
        null=True, blank=True)
    is_club_branded = models.BooleanField(default=False)
    is_casual = models.BooleanField(
        default=False, null=True, blank=True)
    for_training = models.BooleanField(
        default=False, null=True, blank=True)
    is_competitive = models.BooleanField(
        default=False, null=True, blank=True)
    has_sizes = models.BooleanField(
        default=False, null=True, blank=True)
    is_footwear = models.BooleanField(
        default=False, null=True, blank=True)
    is_gendered = models.BooleanField(
        default=False, null=True, blank=True)
    is_equipment = models.BooleanField(
        default=False, null=True, blank=True)
    is_personalised = models.BooleanField(
        default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    reverse_image = models.ImageField(null=True, blank=True)
    reverse_image_url = models.URLField(
        max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=254, default="Unnamed Subcategory")
    casual = models.BooleanField(default=False, null=True, blank=True)
    training = models.BooleanField(default=False, null=True, blank=True)
    competitive = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
