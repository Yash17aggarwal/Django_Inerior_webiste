# from dataclasses import fields
from django import forms
from . models import subscribe

class SubcribersForm(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = ['email', ]