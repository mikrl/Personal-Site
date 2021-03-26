from django.urls import path
from portfolio import views

urlpatterns = [
    #path("", views.portfolio_page, name="portfolio"),
    path('projects/', views.ProjectList.as_view(), name='home'),
    path('<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
]
