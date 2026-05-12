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
class CertificationForm(forms.ModelForm):

    class Meta:
        model = Certification
        fields = '__all__'

class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = '__all__'

class UCForm(forms.ModelForm):

    class Meta:
        model = UC
        fields = '__all__'

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
    
class TFCForm(forms.ModelForm):

    class Meta:
        model = TFC
        fields = '__all__'
        
class TechnologyForm(forms.ModelForm):

    class Meta:
        model = Technology
        fields = '__all__'
        
class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = '__all__'