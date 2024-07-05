from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

class ConversionForm(forms.Form):
    AMOUNT_CHOICES = (
        ('CLP to USD', 'CLP a USD'),
        ('USD to CLP', 'USD a CLP'),
    )
    
    amount = forms.DecimalField(label='Monto', decimal_places=2)
    direction = forms.ChoiceField(choices=AMOUNT_CHOICES, label='Dirección')
