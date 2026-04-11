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

admin.site.register(Project)

admin.site.register(Technology)