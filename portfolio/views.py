from typing import List, Union

from django.views import generic

from .models import Statement
from .models import Project
from .models import Certification



class StatementList (generic.ListView):    
    # queryset_imagelinks = ImageLink.objects.all()
    # queryset = blend(queryset_statements, queryset_imagelinks)
    queryset = Statement.objects.all()
    template_name = 'statements.html'    

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












