from django import forms

from .models import Projects, P_Images

class ProjectsForm(forms.ModelForm):
    
    class Meta:
        model = Projects
        #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ('images','title', 'description', 'files',)


class P_ImageForm(forms.ModelForm):
    #p_image = forms.ImageField(label='Image')  
    class Meta:
        model = P_Images
        fields = ('p_file',)

