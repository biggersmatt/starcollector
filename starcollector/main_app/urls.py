from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stars/', views.stars_index, name='stars'),
    path('stars/<int:star_id>/', views.stars_detail, name='detail'),
    path('stars/<int:star_id>/add_planet/', views.add_planet, name='add_planet')
]
