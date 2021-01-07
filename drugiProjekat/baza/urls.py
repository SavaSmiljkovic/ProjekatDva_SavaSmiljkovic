from django.urls import path
from . import views

app_name = 'baza'
urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:id>/', views.car, name='car'),
    path('car/edit/<int:id>/', views.edit, name='edit'),
    path('car/delete/<int:id>/', views.delete, name='delete'),
    path('car/new/', views.new, name='new'),
    path('accounts/signUp/', views.signUp, name='signUp')
]
