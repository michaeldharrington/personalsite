from django.contrib import admin

from .models import Project
from .models import ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInline, ]

admin.site.register(Project, ProjectAdmin)
