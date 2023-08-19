from django.urls import path
from . import views




urlpatterns = [
    path('',views.index,name='index'),
    path('post/<str:pk>',views.posts,name='post'),
    path('register',views.register,name='register'),
    path('logout', views.logout,name='logout'),
    path('login', views.login,name='login')
   ]