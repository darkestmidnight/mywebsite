from django.urls import re_path, include
from . import views

# urls for home page

urlpatterns = [
    re_path(r'^$', views.index, name="home"),
]