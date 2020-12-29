from django import forms

from .models import Literature

class Literature_form(forms.ModelForm):
    class Meta:
        model= Literature
        fields =[
            'name',
            'title',
            'description',
            'literature'
        ]
