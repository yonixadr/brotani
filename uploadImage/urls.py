from django.urls import path
from uploadImage import views


from .views import FileUploadView

urlpatterns = [
    path('image/upload/', FileUploadView.as_view(), name='file-upload'),
    path('image/detail_image/   ',
         views.detail_image, name='detail-image')


]
