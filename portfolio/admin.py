from django.contrib import admin

from .models import Certification
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified_date', 'slug', 'status')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CertAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiration_date', 'level')
    list_filter = ('level',)
    search_fields = ['title',]

    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Certification, CertAdmin)
