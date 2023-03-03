from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def auto_view(request):
  data={
    'form': AutoForm()
  }

  if request.method == 'POST':
    formulario = AutoForm(data=request.POST,files = request.FILES)
    if formulario.is_valid():
      formulario.save()
      data["mensaje"] = "Información guardada"
    else:
      data["form"] = formulario
  return render(request, 'Auto.html',data)

def propietario_view(request):
  data={
    'form': propietarioForm()
  }

  if request.method == 'POST':
    formulario = propietarioForm(data=request.POST,files = request.FILES)
    if formulario.is_valid():
      formulario.save()
      data["mensaje"] = "Información guardada"
    else:
      data["form"] = formulario
  return render(request, 'Propietario.html',data )

def parqueo_view(request):
  data={
    'form': parqueoForm()
  }

  if request.method == 'POST':
    formulario = parqueoForm(data=request.POST,files = request.FILES)
    if formulario.is_valid():
      formulario.save()
      data["mensaje"] = "Información guardada"
    else:
      data["form"] = formulario
  return render(request, 'Parqueo.html',data )

def listarPropietario(request):
  propietarios = Propietario.objects.all()
  return render(request, 'listarPropietario.html', {'propietarios': propietarios})

def listarAuto(request):
  autos = Auto.objects.all()
  return render(request, 'listarAuto.html', {'autos': autos})

def listarParqueo(request):
  parqueos = Parqueo.objects.all()
  return render(request, 'listarParqueo.html', {'parqueos': parqueos})
