from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Renders all fields except user field
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Name",
            "surname": "Surname",
            "phone_number": "Phone Number",
            "email": "Email",
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
            self.fields[field].widget.attrs["class"] = "profile-form-input"
