from django.db import models

SPECTRAL = (
  ('O', '0'),
  ('B', 'B'),
  ('A', 'A'),
  ('F', 'F'),
  ('G', 'G'),
  ('K', 'K'),
  ('M', 'M'),
)

DESCRIP = (
  ('1', 'Hypergiant'),
  ('2', 'Supergiant'),
  ('3', 'Giant'),
  ('4', 'Subgiant'),
  ('5', 'Dwarf'),
  ('6', 'Subdwarf'),
  ('7', 'White Dwarf'),
)

# Create your models here.
class Star(models.Model):
  name = models.CharField(max_length=100)
  solar_mass = models.FloatField(default=0.0)
  spectral_type = models.CharField(
    max_length=1,
    choices=SPECTRAL,
    default=SPECTRAL[0][0],
  )
  description = models.CharField(
    max_length=1,
    choices=DESCRIP,
    default=DESCRIP[0][0],
  )

  def __str__(self):
    return self.name
  
MASS  = (
  ('1', 'Giant Planet'),
  ('2', 'Ice Giant'),
  ('3', 'Mesoplanet'),
  ('4', 'Mini-Neptune'),
  ('5', 'Planetar'),
  ('6', 'Super-Earth'),
  ('7', 'Super-Jupiter'),
  ('8', 'Sub-Earth'),
)

ORBIT = (
  ('1', 'Circumbinary'),
  ('2', 'Exoplanet'),
  ('3', 'Goldilocks'),
  ('4', 'Pulsar'),
  ('5', 'Rogue'),
)
  
class Planet(models.Model):
  name = models.CharField(max_length=100)
  mass = models.CharField(
    max_length=1,
    choices=MASS,
    default=MASS[0][0]
  )
  orbit = models.CharField(
    max_length=1,
    choices=ORBIT,
    default=ORBIT[0][0]
  )
  
  star = models.ForeignKey(Star, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.name} is a {self.get_mass_display()} mass planet'