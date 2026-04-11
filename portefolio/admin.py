from django.contrib import admin
from .models import *

admin.site.register(Course)

admin.site.register(UC)

# Teacher admin
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'about']
    list_editable = ['about']

admin.site.register(Teacher, TeacherAdmin)

# Technology admin
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description', 'level', 'annotations','link']
    list_editable = ['level', 'annotations', 'link']

admin.site.register(Technology, TechnologyAdmin)

admin.site.register(Project)