from django.urls import path
from . import views

app_name='account'

urlpatterns=[

    path('',views.registration,name="registration"),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),


]