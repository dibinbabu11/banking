from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('log',views.log,name='log'),
    path('logout',views.logout,name='logout'),
    path('new',views.new,name='new'),

]
