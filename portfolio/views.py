from django.views import generic
from .models import Project

class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status__gte=1)
    template_name = 'index.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'
    













