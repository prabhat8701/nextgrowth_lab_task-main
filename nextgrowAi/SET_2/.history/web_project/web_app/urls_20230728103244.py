from django.urls import path
from . import vi
urlpatterns = [
    path("", views.login_page, name='login_page'),
]