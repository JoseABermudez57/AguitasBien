from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.save_water_sample)
]