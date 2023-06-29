from django import forms
from . models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['cart','discount','subtotal','amount','order_status','ref','payment_complete']
        widgets = {
            'order_by':forms.TextInput(attrs={'class':'formcontrol'}),
            'shipping_address':forms.TextInput(attrs={'class':'formcontrol','rows':'3'}),
            'email':forms.TextInput(attrs={'class':'formcontrol'}),
            'mobile':forms.TextInput(attrs={'class':'formcontrol'}),
            'payment_method':forms.TextInput(attrs={'class':'formcontrol'})
        }
