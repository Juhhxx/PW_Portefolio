from django import forms
from .models import *

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
        'name': forms.TextInput(attrs={
            'placeholder':'Course Name',
        })
        } 
        
        help_texts = {
        'retrato': 'Use an image with less than 100kB', 
        }   

