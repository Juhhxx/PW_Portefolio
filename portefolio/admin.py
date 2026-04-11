from django.contrib import admin
from .models import *

# Inlines
class ProjectInline(admin.TabularInline):
    model = Project

admin.site.register(Course)

# Certification admin
admin.site.register(Certification)

# Workshop admin
admin.site.register(Workshop)

# UC admin
class UCAdmin(admin.ModelAdmin):
    search_fields = ['name', 'courses__name']
    list_display = ['name']
    list_filter = ['courses']
    filter_horizontal = ['teachers', 'technologies', 'courses']
    inlines = [ProjectInline]
    
admin.site.register(UC, UCAdmin)

# Teacher admin
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'about']
    list_filter = ['ucs', 'ucs__courses']

admin.site.register(Teacher, TeacherAdmin)

# Technology admin
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'level', 'annotations','link']
    list_editable = ['annotations', 'level']

admin.site.register(Technology, TechnologyAdmin)

# Project admin
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['name', 'uc__name']
    list_display = ['name', 'description', 'uc', 'repository']
    list_editable = ['description']
    list_filter = ['uc', 'technologies']
    filter_horizontal = ['technologies']
    
    
admin.site.register(Project, ProjectAdmin)

# TFC admin
class TFCAdmin(admin.ModelAdmin):
    search_fields = ['name', 'courses__name']
    list_display = ['name', 'description', 'link']
    list_editable = ['description']
    filter_horizontal = ['courses', 'supervisors', 'technologies']
    list_filter = ['courses', 'technologies']
    
admin.site.register(TFC, TFCAdmin)

# Skill admin
admin.site.register(Skill)