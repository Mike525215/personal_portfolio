from django.contrib import admin
from portfolio.models import *
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id']
    ordering = ['id']
admin.site.register(Project, ProjectsAdmin)
