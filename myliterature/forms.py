from django import forms

from .models import Literature

class LiteratureForm(forms.ModelForm):
    class Meta:
        model= Literature
        fields =[
            'name',
            'title',
            'description',
            'literature'
        ]
