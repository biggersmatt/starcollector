from django.shortcuts import render, redirect
from .models import Star
from .forms import PlanetForm

# Create your views here.
def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

def stars_index(request):
  stars = Star.objects.all()
  return render(request, 'stars/index.html', { 'stars': stars })

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
  return redirect('detail', star_id=star_id)