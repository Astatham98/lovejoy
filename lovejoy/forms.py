from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Evaluation
from captcha.fields import CaptchaField



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone_number = forms.CharField(max_length=12, help_text='Enter a valud phone number.')
    captcha = CaptchaField()


    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'phone_number',  'email', 'password1', 'password2', )

class EvaluationsForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['evaluation_text', 'contact_choice', 'image', 'user']

class CaptchForm(forms.Form):
    captcha = CaptchaField()
