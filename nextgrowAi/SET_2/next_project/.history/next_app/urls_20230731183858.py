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

    path('add_android_app/', views.add_android_app, name='add_android_app'),
    path('app_list/', views.app_list, name='app_list'),
    path('app_list1/', views.app_list1, name='app_list1'),

    
    path('app_detail/<int:app_id>/', views.app_detail, name='app_detail'),
    path('add_task_screenshot/', views.add_task_screenshot, name='add_task_screenshot'),
]
