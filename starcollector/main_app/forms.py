from django import forms
from .models import Star, Planet

class StarForm(forms.ModelForm):
  class Meta:
    model = Star
    fields = [
      'name',
      'solar_mass',
      'spectral_type',
      'description',
    ]

class PlanetForm(forms.ModelForm):
  class Meta:
    model = Planet
    fields = ['name', 'size']