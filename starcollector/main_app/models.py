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
  ('1', 'Hypergiants'),
  ('2', 'Supergiants'),
  ('3', 'Giants'),
  ('4', 'Subgiants'),
  ('5', 'Dwarf'),
  ('6', 'Subdwarf'),
  ('7', 'White Dwarf'),
)

# Create your models here.
class Star(models.Model):
  name = models.CharField(max_length=100, default='Enter Star Name')
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
  
SIZES  = (
  ('S', 'Small'),
  ('M', 'Medium'),
  ('L', 'Large')
)
  
class Planet(models.Model):
  name = models.CharField(max_length=100)
  size = models.CharField(
    max_length=1,
    choices=SIZES,
    default=SIZES[0][0]
  )
  
  star = models.ForeignKey(Star, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.name} is a {self.get_size_display()} size planet'