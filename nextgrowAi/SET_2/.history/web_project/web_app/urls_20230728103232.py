from django.urls import path

urlpatterns = [
    path("", views.login_page, name='login_page'),
]