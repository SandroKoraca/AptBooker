from main.models import *
from django.shortcuts import render, redirect    
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login    
from .forms import *
import random

## Create your views here.
def homepage(request):
    apartmani = list(Apartman.objects.all())
    if len(apartmani) >= 4:
        apartmani = random.sample(apartmani, 4)
    else:
        apartmani = random.sample(apartmani, len(apartmani))
    podaci = {
        'random_apartmani': apartmani
    }
    return render(request, 'homepage.html', podaci)

def admin_panel(request):
    return render(request, 'admin/admin_panel.html')

def o_nama(request):
    return render(request, 'o_nama.html')

def odobravanje_apartmana(request):
    svi_apartmani = Apartman.objects.all()
    podaci = {
        'svi_apartmani': svi_apartmani
    }
    return render(request, 'admin/apartman_list.html', podaci)

def moji_apartmani(request):
    svi_apartmani = Apartman.objects.all()
    podaci = {
        'moji_apartmani': svi_apartmani
    }
    return render(request, 'main/moji_apartmani.html', podaci)

def pojedini_apartman(request, pk):
    odredjeni_apartman= Apartman.objects.get(id=pk)
    sve_recenzije = Recenzija.objects.filter(apartman=pk)
    podaci = {
        'apartman': odredjeni_apartman,
        'recenzije': sve_recenzije,
        'pk': pk
    }
    return render(request, 'main/apartman_odredjeni.html', context=podaci)

class ApartmanList(ListView):
    model = Apartman

class ApartmanLDetailView(DetailView):
    model = Apartman

def dodavanje_apartmana(request):
    form = ApartmanForm()
    if request.method == "POST":
        form = ApartmanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/apartmani")

    context = {"form": form}
    return render(request, 'main/apartman_create.html', context=context)

def uredivanje_apartmana(request, pk):
    odabrani_apartman = Apartman.objects.get(id=pk)
    form = ApartmanForm(instance=odabrani_apartman)
    if request.method == "POST":
        form = ApartmanForm(request.POST, instance=odabrani_apartman)
        if form.is_valid():
            form.save()
            return redirect("/apartmani/"+str(pk))

    context = {"form": form}
    return render(request, 'main/apartman_create.html', context=context)

def brisanje_apartmana(request, pk):
    odabrani_apartman = Apartman.objects.get(id=pk)
    if request.method == "POST":
        odabrani_apartman.delete()
        return redirect("/apartmani")

    context = {"apartman": odabrani_apartman}
    return render(request, "main/apartman_delete.html", context)

def pisanje_recenzije(request, pk):
    form = RecenzijaForm()
    if request.method == "POST":
        form = RecenzijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/apartmani/"+str(pk))

    context = {"form": form, "pk":pk}
    return render(request, 'main/pisanje_recenzije.html', context=context)

def odobravanje_odredjenog_apartmana(request, pk):
    odredjeni_apartman = Apartman.objects.get(id=pk)
    form = ApartmanForm(instance=odredjeni_apartman)
    if request.method == "POST":
        form = ApartmanForm(request.POST, instance=odredjeni_apartman)
        if form.is_valid():
            form.save()
            return redirect("/adminpanel/OdobravanjeApartmana")

    context = {"form": form, "pk":pk}
    return render(request, 'admin/apartman_odobravanje.html', context=context)