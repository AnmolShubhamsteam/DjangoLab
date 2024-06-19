from django import forms
from core.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=Project
        fields ="__all__"
        