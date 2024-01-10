from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserTypeForm(forms.ModelForm):
    is_doctor = forms.BooleanField(label='Are you a doctor?', required=False, widget=forms.CheckboxInput)
    class Meta:
        model = UserProfile
        profile_picture = forms.ImageField(required=False)
        address_line1 = forms.CharField(max_length=255)
        city = forms.CharField(max_length=100)
        state = forms.CharField(max_length=100)
        pincode = forms.CharField(max_length=10)
        fields = ['is_doctor','address_line1','city','state','pincode','profile_picture']
