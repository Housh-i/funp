from django import forms
from django.core.exceptions import ValidationError
from contacts.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Enter contact name",
            }
        ),
        max_length=100,
        required=True,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Enter contact email",
            }
        )
    )

    document = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "class": "file-input file-input-bordered w-full",
            }
        ),
        required=False,
    )

    def clean_name(self):
        name = self.cleaned_data["name"]
        # Check if the name already exists for this user
        if name.startswith("X"):
            raise ValidationError("No names beginning with X!")
        return name

    def clean_email(self):
        email = self.cleaned_data["email"]
        # Check if the email already exists for this user
        if Contact.objects.filter(user=self.initial.get("user"), email=email).exists():
            raise ValidationError("You already have a contact with this email address.")
        return email

    class Meta:
        model = Contact
        fields = ("name", "email", "document")
