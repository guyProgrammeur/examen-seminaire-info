from django.db import models
from django.db import models

class Faculte(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20, unique=True)
    date_naissance = models.DateField()
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    adresse = models.TextField()
    faculte = models.ForeignKey(Faculte, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
