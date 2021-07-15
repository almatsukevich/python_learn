from django import forms
from . import models


class OrderCreateForm(forms.Form):
    customer_name = forms.CharField(
        label="Имя", 
        required=True,
        widget=forms.TextInput)

    customer_phone = forms.CharField(
        label="Телефон", 
        required=True,
        widget=forms.TextInput,
        help_text="+375291234567"
        )

    contact_info = forms.CharField(
        label="Адрес",  
        widget=forms.TextInput)

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'status',
            'customer_name',
            'customer_phone',
            'contact_info']