from django.urls import re_path, include
from . import views

# urls for projects page


urlpatterns = [
    re_path(r'^$', views.index, name="contact"),
]