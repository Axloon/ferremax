from django import forms

class ConversionForm(forms.Form):
    AMOUNT_CHOICES = (
        ('CLP to USD', 'CLP a USD'),
        ('USD to CLP', 'USD a CLP'),
    )
    
    amount = forms.DecimalField(label='Monto', decimal_places=2)
    direction = forms.ChoiceField(choices=AMOUNT_CHOICES, label='Dirección')
