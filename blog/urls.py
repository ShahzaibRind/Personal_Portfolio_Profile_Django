from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_blog, name="home_blog"),
    path('int:<blog>', views.home_blog, name="home_blog"),
]