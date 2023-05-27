
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('export/', views.export_data, name='export'),
    path('import/', views.importData, name='import_data'),
    
]
