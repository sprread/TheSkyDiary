from django import forms

from .models import Customer


class PostCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'notes', 'phone_number')


class ExistingCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('notes',)



