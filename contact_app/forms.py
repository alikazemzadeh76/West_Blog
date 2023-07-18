from django import forms
from django.core.validators import ValidationError
from .models import DeliverMassage





class ContactUsForm(forms.ModelForm):
    class Meta:
        model = DeliverMassage
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "enter your email",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter subject",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "enter your message",
            })
        }


