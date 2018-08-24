from django.shortcuts import render, redirect, reverse,get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views import View

from .models import Projects, P_Images
from .forms import ProjectsForm, P_ImageForm

# Create your views here.
# Function to create projects

class CreateProjectsView(View):
    def get(self, request):
        p_photos = P_Images.objects.all()
        #project_form = ProjectsForm(initial=self.initial)
        project_form = ProjectsForm()
        context = {
            'p_photos': p_photos,
            'project_form': project_form,
        }
        return render(self.request, 'projects/forms.html', context)

    def post(self, request):
        project_form = ProjectsForm(request.POST, request.FILES)
        multi_img_form = P_ImageForm(request.POST, request.FILES)

        if project_form.is_valid():
            instance = project_form.save(commit=False)
            instance.user = request.user
            instance.save()

        if multi_img_form.is_valid():   
            #instance = project_form.save(commit=False)
            #instance.user = request.user
            #instance.save()
            images = multi_img_form.save(commit=False)
            images.save()

            data = {
                'is_valid': True, 
                'name': images.p_file.name, 
                'url': images.p_file.url
            }

        else:
            data = {
                'is_valid': False,
            }

        return JsonResponse(data)

        #actual_p = Projects.feature_images()
        #actual_p.save()
        #f_images = P_Images(fk_post=actual_p)
        #f_images.save()



# Function to retrieve all different projects
def retrieve_projects(request):
    # Retrieves objects based on latest publish date
    projects_list = Projects.objects.all().order_by("-publish_date")
    context = {
        'projects_list': projects_list,
    }
    return render(request, 'projects/projects.html', context)

# Function to update projects
def update_projects(request, slug):
    instance = get_object_or_404(Projects, slug=slug)
    project_form = ProjectsForm(request.POST or None, instance=instance)
    
    # Update_date becomes the latest time
    if project_form.is_valid():
        project_form.save()
    #    return redirect('retrieve_projects')
    context = {
        'instance': instance,
        'project_form': project_form
    }
    return render(request, 'projects/forms.html', context)

# Function to delete projects chosen
def delete_projects(request, slug):
    Projects.objects.filter(slug=slug).delete()
    return redirect('retrieve_projects')

# Function to show details of project using the ids
def details_of_project(request, slug):
    # Will raise 404 if there is not such id
    project_details = get_object_or_404(Projects, slug=slug)
    context = {
        'project_details': project_details,
    }
    return render(request, 'projects/posts.html', context)


