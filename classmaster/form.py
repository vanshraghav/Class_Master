# forms.py

from django import forms
from .models import Faculty, Class, Subject

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
