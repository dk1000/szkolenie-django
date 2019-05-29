from datetime import datetime

from django import forms
from contact.models import Person


class PersonForm(forms.ModelForm):
    def clean_date_of_birth(self):
        date_of_birth = self.data['date_of_birth']
        return datetime.strptime(date_of_birth, '%Y-%d-%m').date()

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'date_of_birth']
