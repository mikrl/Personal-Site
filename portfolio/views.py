from typing import List, Union

from django.views import generic

from .models import Statement
from .models import Project
from .models import Certification



class FrontPage (generic.TemplateView):
    queryset_statements = Statement.objects.all()
    # queryset_imagelinks = ImageLink.objects.all()
    # queryset = blend(queryset_statements, queryset_imagelinks)
    template_name = 'index.bootstrap.html'    

class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status__gte=1)
    template_name = 'projects.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'

class CertificationList(generic.ListView):
    #breakpoint()
    queryset = Certification.objects.all()
    template_name = 'certifications.html'

class CertificationDetail(generic.DetailView):
    model = Certification
    template_name = 'certification_detail.html'
    













