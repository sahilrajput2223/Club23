from  django import forms
from .models import Bookclub

class DateInput(forms.DateInput):
    input_type = 'Date'
    format = '%m/%d/%Y'
    input_formats = '%m/%d/%Y'

class TimeInput(forms.TimeInput):
    input_type = 'Time'

class Bookclub_from(forms.ModelForm):
    class Meta:
        model = Bookclub
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'Occasion': forms.Select(attrs={'placeholder': 'Select Occasion', 'class': 'form-control'}),
            'Time_from': TimeInput(attrs={'placeholder': 'Select Time From', 'class': 'form-control'}),
            'Time_to': TimeInput(attrs={'placeholder': 'Select Time To', 'class': 'form-control'}),
            'Date_from': DateInput(attrs={'placeholder': 'Select Date From', 'class': 'form-control'}),
            'Date_to': DateInput( attrs={'placeholder': 'Select Date From', 'class': 'form-control'}),
            'Venu': forms.Select(attrs={'placeholder': 'Select Venu', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(Bookclub_from, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['Occasion'].label = 'Occasion'
        self.fields['Time_from'].label = 'Time From'
        self.fields['Time_to'].label = 'Time To'
        self.fields['Date_from'].label = 'Date From'
        self.fields['Date_to'].label = 'Date To'
        self.fields['Venu'].label = 'Venu'
