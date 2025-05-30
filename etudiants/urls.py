from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('etudiants/', liste_etudiants, name='liste_etudiants'),
    path('etudiants/ajouter/', ajouter_etudiant, name='ajouter_etudiant'),
]
