from django.db import models

# Create your models here.
def image_path(instance, filename):
    return (str(instance.id)+"/"+filename)

class Apartman(models.Model):
    apartman_naziv = models.CharField(max_length=100)
    apartman_cijena = models.FloatField()
    apartman_vlasnik = models.CharField(max_length=100)
    apartman_smjestaji = models.IntegerField()
    apartman_lokacija = models.CharField(max_length=100)
    apartman_odobren = models.BooleanField(default=False)
    apartman_sadrzaj = models.TextField()
    apartman_glavna_slika = models.ImageField(upload_to="", blank=True, null=True)

class Recenzija(models.Model):
    autor = models.CharField(max_length=100)
    apartman = models.CharField(max_length=10)
    sadrzaj = models.TextField()
    ocjena = models.IntegerField()