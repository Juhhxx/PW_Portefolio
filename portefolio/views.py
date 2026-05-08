from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index_view(request):

    return render(request, 'portfolio/index.html')

def educations_view(request):

    context = {
        'courses': Course.objects.all(),
        'certifications': Certification.objects.all(),
        'workshops': Workshop.objects.all()
    }

    context['gestor'] = request.user.groups.filter(name='gestor_portefolio').exists()

    return render(request, 'portfolio/education.html', context)

def course_view(request, course_id):

    context = { 'course': Course.objects.get(id = course_id)}

    return render(request, 'portfolio/course.html', context)

@login_required
def new_course_view(request):

    form = CourseForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portfolio:educations')
    
    context = {'form': form}
    return render(request, 'portfolio/new_course.html', context)

@login_required
def edit_course_view(request, course_id):

    course = Course.objects.get(id = course_id)
    
    if request.POST:
        form = CourseForm(request.POST or None, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('portfolio:educations')
    else:
        form = CourseForm(instance=course)
        
    context = {'form': form, 'course':course}
    return render(request, 'portfolio/edit_course.html', context)

@login_required
def delete_course_view(request, course_id):

    course = Course.objects.get(id = course_id)
    course.delete()
    return redirect('portfolio:educations')