from django.urls import path
from next_app import views

app_name='gradesApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('registeradmin/',views.registeradmin,name='registeradmin'),
    path('registeruser/',views.registerTeacher,name='registerTeacher'),
    path('login/',views.userLogin,name='userLogin'),
    path('dashboard',views.dashboard,name='dashboard'),
   
]
