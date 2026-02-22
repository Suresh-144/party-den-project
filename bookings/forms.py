from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'event_date', 'message']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
        }