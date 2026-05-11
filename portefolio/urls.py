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
    path('education/course/teacher/new/<int:uc_id>', views.new_teacher_view, name="new_teacher"),
    path('education/course/teacher/delete/<int:teacher_id>/', views.delete_teacher_view, name="delete_teacher"),
    path('education/course/teacher/edit/<int:teacher_id>/', views.edit_teacher_view, name="edit_teacher"),

    path('projects/', views.projects_view, name='projects'),
]
