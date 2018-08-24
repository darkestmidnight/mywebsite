from django.urls import re_path, include
from . import views

# urls for projects page
app_name = 'create_post'

urlpatterns = [
    re_path(r'^$', views.retrieve_projects, name="retrieve_projects"),
    #re_path(r'^create/$', views.CreateProjectsView.as_view(), name="create_projects"),
    re_path(r'^create/$', views.CreateProjectsView.as_view(), name="create_projects"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.details_of_project, name="details_of_project"),
    re_path(r'^(?P<slug>[\w-]+)/update/$', views.update_projects, name="update_projects"),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.delete_projects, name="delete_projects"),
]