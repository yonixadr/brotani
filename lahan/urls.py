from django.urls import path
from lahan import views
urlpatterns = [
    path('lahan/<int:pk>', views.add_lahan, name='add-lahan'),
    path('lahan/list_lahan', views.list_lahan, name='list-lahan'),
    path('lahan/detail_lahan/<int:pk>', views.detail_lahan, name='detail-lahan')

]
