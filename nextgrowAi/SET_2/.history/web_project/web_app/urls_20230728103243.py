from django.urls import path
from . import 
urlpatterns = [
    path("", views.login_page, name='login_page'),
]