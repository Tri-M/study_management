from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    sponsor = forms.CharField(widget=forms.TextInput(attrs={
        'list': 'sponsor-list',  # Links to the datalist in the template
    }))

    class Meta:
        model = Study
        fields = ['name', 'phase', 'sponsor', 'description']
        widgets = {
            'phase': forms.Select(choices=Study.PHASE_CHOICES),  # Dropdown for phase
        }
