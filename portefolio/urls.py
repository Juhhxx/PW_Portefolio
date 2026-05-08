from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('education/', views.educations_view, name='educations'),
    path('course/<int:course_id>/', views.course_view, name="course"),
    path('course/new/', views.new_course_view, name="new_course"),
    path('course/delete/edit/<int:course_id>/', views.delete_course_view, name="delete_course"),
    path('course/edit/<int:course_id>/', views.edit_course_view, name="edit_course"),
]
