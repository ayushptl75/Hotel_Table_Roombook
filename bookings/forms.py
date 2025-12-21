from django import forms
from .models import RoomBooking, TableBooking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['check_in','check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type':'date'}),
            'check_out': forms.DateInput(attrs={'type':'date'}),
        }

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = ['date','time','end_time','guests']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'time': forms.TimeInput(attrs={'type':'time'}),
            'end_time': forms.TimeInput(attrs={'type':'time'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
