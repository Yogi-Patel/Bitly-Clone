from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        # You give a meta class so Django ModelForms knows what model to use and which fields to add in the form
        model = Link
        fields = ['name', 'url', 'slug']