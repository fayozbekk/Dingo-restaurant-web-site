from django import forms

from dingoapp.models import BookingModel


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name *'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number *',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'num_of_g': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of guests *',
                'type': 'number'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date * (yyyy-mm-dd)'
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Time * (hh:mm)',
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'Textarea',
                'rows': '4',
                'placeholder': 'Your Note *'
            })

        }
