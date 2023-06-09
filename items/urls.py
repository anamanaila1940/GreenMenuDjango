from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="starters"),
    path('navbar', views.navbar),
    path('pizza/', views.pizza, name="pizza"),
    path('sides/',views.sides, name="sides"),
    path('dessert/',views.dessert, name="dessert"),
    path('localgood/',views.localgoods, name="localgood"),
    path('tgtb/',views.tgtb, name="tgtb"),
    path('mistake/',views.mistake, name="mistake"),
]

