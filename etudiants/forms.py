from django import forms
from .models import Etudiant,Faculte

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'

class FaculteForm(forms.ModelForm):
    class Meta:
        model = Faculte
        fields = ['nom', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }