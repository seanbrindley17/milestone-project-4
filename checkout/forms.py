from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # Fields here only those which will not be automatically filled/calculated
        fields = (
            "name",
            "surname",
            "email",
            "phone_number",
            "address_line_one",
            "address_line_two",
            "town_or_city",
            "postcode",
            "county",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Name",
            "surname": "Surname",
            "email": "Email",
            "phone_number": "Phone Number",
            "postcode": "Postcode",
            "town_or_city": "Town Or City",
            "address_line_one": "Address Line 1",
            "address_line_two": "Address Line 2",
            "county": "County",
        }

        # Sets the cursor autofocus to the "name" field when page is loaded
        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                # Adds a * to required fields
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            # Removes default form field labels
            self.fields[field].label = False
