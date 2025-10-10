from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  #adding new route for card index
  path('cards/', views.card_index, name='card-index'),
]


# main_app/urls.py
# This file defines URL patterns for the main_app application
# It connects URL paths to their corresponding view functions in views.py
#the url in catcollector/urls.py will point to this file for more routes
