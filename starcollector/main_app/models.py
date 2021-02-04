from django.db import models

# Create your models here.
class Star(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  
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