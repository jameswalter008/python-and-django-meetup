from django import forms
from django.db.models import fields
from django.forms.forms import Form

from .models import Participants

class RegistrationForm(forms.Form):
    email=forms.EmailField(label='Your Email')

    