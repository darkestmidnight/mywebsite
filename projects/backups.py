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
        project_form = ProjectsForm(request.POST or None, request.FILES or None)
        p_formset = P_ImageForm(request.POST, request.FILES)

        # Checks if the project_form is valid before save
        if project_form.is_valid():
            instance = project_form.save(commit=False)
            instance.user = request.user
            instance.save()

        # Checks if multiple image upload is valid before save
        if p_formset.is_valid(): 
        #if project_form.is_valid() and p_formset.is_valid():   
            #instance = project_form.save(commit=False)
            #instance.user = request.user
            #instance.save()
            images = p_formset.save(commit=False)
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