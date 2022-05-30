from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']


class VrSpaceForm(forms.ModelForm):
    class Meta:
        model=VrSpace
        fields=['audio_field','image_field']