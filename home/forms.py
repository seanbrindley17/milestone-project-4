from django import forms
from .models import Product, Category


# Form for admin user to modify store products
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [
            (category.id, category.get_display_name()) for category in categories
        ]

        self.fields["category"].choices = display_names
