from django.urls import path
from aktuator import views
urlpatterns = [
    path('aktuator/<int:pk>', views.add_aktuator, name='add-aktuator'),
    path('aktuator/list_aktuator',
         views.list_aktuator, name='list-aktuator'),

]
