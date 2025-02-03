from django import forms
from .models import Product, Category, Newsletter


# Form for admin user to modify store products
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # Makes the footwear option not selectable
        # Will implement in future but I ran out of time
        excude = ("is_footwear",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [
            (category.id, category.get_display_name()) for category in categories
        ]

        self.fields["category"].choices = display_names


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
