from django import forms
from .models import Stat, Sale



class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ['date', 'stat']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['date', 'amount']  
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a sale date',
                    'type': 'date'
                }
            ),
        }