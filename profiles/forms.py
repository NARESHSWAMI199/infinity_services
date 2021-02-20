from django import forms
from django.forms import ModelForm, fields
from .models import Profile


class ProfileForm(ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model  = Profile
        fields = [
            'image',
            'first_name',
            'last_name',
            'ref_code',
        ]