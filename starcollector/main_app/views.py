from django.shortcuts import render
from django.http import HttpResponse

class Star:
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age
    
stars = [
  Star('Name', 'Description', 'Age'),
]

# Create your views here.
def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

def stars(request):
  return render(request, 'stars/index.html', { 'stars': stars })