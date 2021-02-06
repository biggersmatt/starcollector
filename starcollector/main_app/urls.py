from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stars/', views.stars_index, name='stars'),
    path('stars/add_star/', views.add_star, name='add_star'),
    path('stars/<int:star_id>/', views.stars_detail, name='detail_star'),
    path('stars/<int:star_id>/edit/', views.edit_star, name='edit_star'),
    path('stars/<int:star_id>/delete/', views.delete_star, name='delete_star'),
    path('stars/<int:star_id>/add_planet/', views.add_planet, name='add_planet'),
    path('stars/<int:star_id>/planet/<int:planet_id>/', views.detail_planet, name='detail_planet'),
    path('stars/<int:star_id>/planet/<int:planet_id>/delete/', views.delete_planet, name='delete_planet'),
]
