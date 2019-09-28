from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'email_address',
            'first_name',
            'message',
            'checkbox'

        ]

        