from django.shortcuts import render, redirect
from .models import Etudiant
from .forms import EtudiantForm

def home(request):
    return render(request, 'home.html')


def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'liste_etudiants.html', {'etudiants': etudiants})

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'ajouter_etudiant.html', {'form': form})
