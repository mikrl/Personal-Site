from django.urls import path
from portfolio import views

urlpatterns = [
    path(r'', views.FrontPage.as_view(), name='home'),
    path(r'certifications/', views.CertificationList.as_view(), name='certifications'),
    path('projects/', views.ProjectList.as_view(), name='projects'),
    path('projects/<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
] 
