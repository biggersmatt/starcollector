from django.shortcuts import render, redirect
from .models import Star, Planet
from .forms import StarForm, PlanetForm

# Create your views here.
def home(request):
  return render(request, 'homepage.html')

def about(request):
  return render(request, 'about.html')

def stars_index(request):
  stars = Star.objects.all()
  star_form = StarForm()
  return render(request, 'stars/index.html', {
    'stars': stars,
    'star_form': star_form,
  })
  
def add_star(request):
  form = StarForm(request.POST)
  if form.is_valid():
    new_star = form.save(commit=False)
    new_star.save()
  return redirect('stars')

def edit_star(request, star_id):
  star = Star.objects.get(id=star_id)
  if request.method == 'GET':
    star_form = StarForm(instance=star)
    return render(request, 'stars/edit.html', {
      'form':star_form,
      'star': star })
  else:
    star_form = StarForm(request.POST, instance=star)
    if star_form.is_valid():
      star_form.save()
      return redirect('detail_star', star_id)

def delete_star(request, star_id):
  if request.method == 'POST':
    Star.objects.get(id=star_id).delete()
  return redirect('stars')

def stars_detail(request, star_id):
  star = Star.objects.get(id=star_id)
  planet_form = PlanetForm()
  return render(request, 'stars/detail.html', { 
    'star': star,
    'planet_form': planet_form
  })
  
def add_planet(request, star_id):
  form = PlanetForm(request.POST)
  if form.is_valid():
    new_planet = form.save(commit=False)
    new_planet.star_id = star_id
    new_planet.save()
  return redirect('detail_star', star_id=star_id)

def detail_planet(request, star_id, planet_id):
  star = Star.objects.get(id=star_id)
  planet = Planet.objects.get(id=planet_id)
  if request.method == 'GET':
    planet_form = PlanetForm(instance=planet)
    return render(request, 'planets/detail.html', {
      'form':planet_form,
      'star':star,
      'planet':planet,
    })
    
def edit_planet(request, star_id, planet_id):
  star = Star.objects.get(id=star_id)
  planet = Planet.objects.get(id=planet_id)
  if request.method == 'GET':
    planet_form = PlanetForm(instance=planet)
    return render(request, 'planets/edit.html', {
      'form':planet_form,
      'star': star,
      'planet': planet})
  else:
    planet_form = PlanetForm(request.POST, instance=planet)
    if planet_form.is_valid():
      planet_form.save()
      return redirect('detail_planet', star_id, planet_id)
    
def delete_planet(request, star_id,planet_id):
  if request.method == 'POST':
    Planet.objects.get(id=planet_id).delete()
  return redirect('detail_star', star_id=star_id)