from django.urls import path
from temperatur import views
urlpatterns = [
    path('temperatur/<int:pk>', views.add_temperatur, name='add-temperatur'),
    path('temperatur/list_temperatur',
         views.list_temperatur, name='list-temperatur'),

]
