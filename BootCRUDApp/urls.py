from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addItem/', views.addItem, name='addItem'),
    path('editItem/<int:id>/', views.editItem, name='editItem'),
]

