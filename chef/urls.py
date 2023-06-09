from django.urls import path
from . import views




urlpatterns = [
    path('', views.index),
    path('navbar', views.navbar),
    path('index', views.index, name = "index"),
    path('update/<int:id>', views.update, name = "update"),
    path('mistakes',views.mistakes, name = "success"),
    path('create_mistake/<int:id>', views.createMistake, name = "createMistake"),
    path('createlocal', views.localgoods, name='createlocal'),

]
