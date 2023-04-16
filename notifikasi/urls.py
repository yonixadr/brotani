from django.urls import path
from notifikasi import views
urlpatterns = [
    # path('notifikasi/<int:pk>', views.add_notifikasi, name='add-lahan'),
    path('notifikasi/list_notifikasi/',
         views.list_notifikasi, name='notifikasi')


]
