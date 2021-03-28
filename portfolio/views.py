from django.views import generic

from .models import Project
from .models import Certification



class Homepage (generic.TemplateView):
    template_name = 'index.html'

class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status__gte=1)
    template_name = 'projects.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'

class CertificationList(generic.ListView):
    queryset = Certification.objects.all()
    template_name = 'certifications.html'

class CertificationDetail(generic.DetailView):
    model = Certification
    template_name = 'certification_detail.html'
    













