from django.contrib import admin

from .models import Certification
from .models import Project
from .models import Statement
# Register your models here.

class StatementAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'url_info')
    search_fields = ['title', 'content']

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
admin.site.register(Statement, StatementAdmin)
