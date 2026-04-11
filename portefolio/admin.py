from django.contrib import admin
from .models import *

# Inlines
class ProjectInline(admin.TabularInline):
    model = Project

# Course admin
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'from_year', 'to_year', 'school__acronym']
    list_filter = ['school__acronym', 'school__institution']
    
admin.site.register(Course, CourseAdmin)

# Certification admin
class CertificationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'from_year', 'institution', 'certificate']
    list_filter = ['institution']
    
admin.site.register(Certification, CertificationAdmin)

# Workshop admin
class WorkshopAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'from_year', 'institution']
    list_filter = ['institution']
    
admin.site.register(Workshop, WorkshopAdmin)

# Institution admin
admin.site.register(Institution)

# School admin
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['acronym', 'name', 'institution', 'link']
    list_filter = ['institution']
    
admin.site.register(School, SchoolAdmin)

# UC admin
class UCAdmin(admin.ModelAdmin):
    search_fields = ['name']
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
    search_fields = ['name']
    list_display = ['name', 'description', 'uc', 'repository']
    list_editable = ['description']
    list_filter = ['uc', 'technologies']
    filter_horizontal = ['technologies']
    
    
admin.site.register(Project, ProjectAdmin)

# TFC admin
class TFCAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description', 'link']
    list_editable = ['description']
    filter_horizontal = ['courses', 'supervisors', 'technologies']
    list_filter = ['courses', 'technologies']
    
admin.site.register(TFC, TFCAdmin)

# Skill admin
class SkillAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'description', 'level']
    list_editable = ['description', 'level']
    filter_horizontal = ['technologies', 'projects', 'tfcs']
    
admin.site.register(Skill, SkillAdmin)