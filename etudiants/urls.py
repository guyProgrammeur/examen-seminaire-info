from django.urls import path
from .views import home,liste_etudiants,ajouter_etudiant,ajouter_faculte

urlpatterns = [
    path('', home, name='home'),
    path('etudiants/', liste_etudiants, name='liste_etudiants'),
    path('etudiants/ajouter/', ajouter_etudiant, name='ajouter_etudiant'),
    path('faculte/ajouter/', ajouter_faculte, name='ajouter_faculte'),
]
