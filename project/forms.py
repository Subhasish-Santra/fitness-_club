from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'age', 'gender', 'email', 'password', 'address']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Registration.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')
        return email
