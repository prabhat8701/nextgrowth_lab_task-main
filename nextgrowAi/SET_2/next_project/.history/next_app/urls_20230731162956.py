from django.urls import path
from next_app import views

# app_name='gradesApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),

    path('registeradmin/',views.registeradmin,name='registeradmin'),
    path('registeruser/',views.registeruser,name='registeruser'),

    path('login/',views.userLogin,name='userLogin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_app/', views.add_android_app, name='add_android_app')
]
