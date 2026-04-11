from django.contrib import admin
from .models import *

admin.site.register(Course)

# UC admin
class UCAdmin(admin.ModelAdmin):
    search_fields = ['name', 'courses__name']
    list_display = ['name']
    list_filter = ['courses']    
    
admin.site.register(UC, UCAdmin)

# Teacher admin
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'about']

admin.site.register(Teacher, TeacherAdmin)

# Technology admin
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'level', 'annotations','link']
    list_editable = ['annotations', 'level']

admin.site.register(Technology, TechnologyAdmin)

admin.site.register(Project)