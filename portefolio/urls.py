from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    
    path('education/', views.educations_view, name='educations'),

    path('education/course/<int:course_id>/', views.course_view, name="course"),
    path('education/course/new/', views.new_course_view, name="new_course"),
    path('education/course/delete/<int:course_id>/', views.delete_course_view, name="delete_course"),
    path('education/course/edit/<int:course_id>/', views.edit_course_view, name="edit_course"),

    path('education/certification/<int:certification_id>/', views.certification_view, name="certification"),
    path('education/certification/new/', views.new_certification_view, name="new_certification"),
    path('education/certification/delete/<int:certification_id>/', views.delete_certification_view, name="delete_certification"),
    path('education/certification/edit/<int:certification_id>/', views.edit_certification_view, name="edit_certification"),

    path('education/workshop/<int:workshop_id>/', views.workshop_view, name="workshop"),
    path('education/workshop/new/', views.new_workshop_view, name="new_workshop"),
    path('education/workshop/delete/<int:workshop_id>/', views.delete_workshop_view, name="delete_workshop"),
    path('education/workshop/edit/<int:workshop_id>/', views.edit_workshop_view, name="edit_workshop"),

    path('education/course/uc/<int:uc_id>/', views.uc_view, name="uc"),
    path('education/course/uc/new/', views.new_uc_view, name="new_uc"),
    path('education/course/uc/delete/<int:uc_id>/', views.delete_uc_view, name="delete_uc"),
    path('education/course/uc/edit/<int:uc_id>/', views.edit_uc_view, name="edit_uc"),

    path('education/course/teacher/<int:teacher_id>/', views.teacher_view, name="teacher"),
    path('education/course/teacher/new/<int:uc_id>/', views.new_teacher_uc_view, name="new_teacher"),
    path('education/tfc/teacher/new/<int:tfc_id>/', views.new_teacher_tfc_view, name="new_teacher"),
    path('education/teacher/delete/<int:teacher_id>/', views.delete_teacher_view, name="delete_teacher"),
    path('education/course/<int:course_id>/teacher/delete/<int:teacher_id>/', views.delete_teacher_course_view, name="delete_teacher_course"),
    path('projects/tfc/<int:tfc_id>/teacher/delete/<int:teacher_id>/', views.delete_teacher_tfc_view, name="delete_teacher_tfc"),
    path('education/course/teacher/edit/<int:teacher_id>/', views.edit_teacher_view, name="edit_teacher"),

    path('projects/', views.projects_view, name='projects'),

    path('projects/project/<int:project_id>/', views.project_view, name="project"),
    path('projects/project/new/', views.new_project_view, name="new_project"),
    path('projects/<int:skill_id>/project/new/', views.new_project_skill_view, name="new_project_skill"),
    path('projects/project/delete/<int:project_id>/', views.delete_project_view, name="delete_project"),
    path('projects/project/edit/<int:project_id>/', views.edit_project_view, name="edit_project"),
    
    path('projects/tfc/<int:tfc_id>/', views.tfc_view, name="tfc"),
    path('projects/tfc/new/', views.new_tfc_view, name="new_tfc"),
    path('projects/<int:skill_id>/tfc/new/', views.new_tfc_skill_view, name="new_tfc_skill"),
    path('projects/tfc/delete/<int:tfc_id>/', views.delete_tfc_view, name="delete_tfc"),
    path('projects/tfc/edit/<int:tfc_id>/', views.edit_tfc_view, name="edit_tfc"),
    
    path('technology/<int:technology_id>/', views.technology_view, name="technology"),
    path('project/technology/new/<int:project_id>', views.new_technology_project_view, name="new_technology_project"),
    path('tfc/technology/new/<int:tfc_id>', views.new_technology_tfc_view, name="new_technology_tfc"),
    path('project/technology/delete/<int:technology_id>/', views.delete_technology_view, name="delete_technology"),
    path('project/technology/delete/<int:project_id>/<int:technology_id>/', views.delete_technology_project_view, name="delete_technology_project"),
    path('tfc/technology/delete/<int:tfc_id>/<int:technology_id>/', views.delete_technology_tfc_view, name="delete_technology_tfc"),
    path('technology/edit/<int:technology_id>/', views.edit_technology_view, name="edit_technology"),

    path('skills/', views.skills_view, name='skills'),
    
    path('skills/skill/<int:skill_id>/', views.skill_view, name="skill"),
    path('skills/skill/new/', views.new_skill_view, name="new_skill"),
    path('skills/skill/delete/<int:skill_id>/', views.delete_skill_view, name="delete_skill"),
    path('skills/skill/edit/<int:skill_id>/', views.edit_skill_view, name="edit_skill"),
    
    path('makingof/', views.makingof_view, name='makingof'),
]
