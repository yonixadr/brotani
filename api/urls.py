from .views import RegisterAPI, LoginAPI, ChangePasswordView, logout
from django.urls import path
from knox import views as knox_views
from api import views
from api.views import UserAPiView


urlpatterns = [
    path('register/', views.RegisterAPI, name='register'),
    path('api/login/', views.LoginAPI, name='login'),
    # path('logout/', LogoutView.as_view, name='logout'),
    path('logout/', views.logout, name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPiView.as_view(), name='user'),
    path('user/all/', views.getAlluser, name='getAlluser'),
    path('user/detail/', views.getDetailuser, name='getDetailuser'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(),
         name='auth_change_password'),
]
