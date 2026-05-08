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
        'workshops': Workshop.objects.all(),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/education.html', context)

# Course views

def course_view(request, course_id):

    context = { 
        'course': Course.objects.get(id = course_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

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
            return redirect('portfolio:course', course_id = course.id)
    else:
        form = CourseForm(instance=course)
        
    context = {'form': form, 'course':course}
    return render(request, 'portfolio/edit_course.html', context)

@login_required
def delete_course_view(request, course_id):

    course = Course.objects.get(id = course_id)
    course.delete()
    return redirect('portfolio:educations')

# Certification views

def certification_view(request, certification_id):

    context = {
        'certification': Certification.objects.get(id = certification_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/certification.html', context)

@login_required
def new_certification_view(request):

    form = CertificationForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portfolio:educations')
    
    context = {'form': form}
    return render(request, 'portfolio/new_certification.html', context)

@login_required
def edit_certification_view(request, certification_id):

    certification = Certification.objects.get(id = certification_id)
    
    if request.POST:
        form = CertificationForm(request.POST or None, request.FILES, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('portfolio:certification', certification_id = certification.id)
    else:
        form = CertificationForm(instance=certification)
        
    context = {'form': form, 'certification':certification}
    return render(request, 'portfolio/edit_certification.html', context)

@login_required
def delete_certification_view(request, certification_id):

    certification = Certification.objects.get(id = certification_id)
    certification.delete()
    return redirect('portfolio:educations')

# Workshop views

def workshop_view(request, workshop_id):

    context = {
        'workshop': Workshop.objects.get(id = workshop_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/workshop.html', context)

@login_required
def new_workshop_view(request):

    form = WorkshopForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portfolio:educations')
    
    context = {'form': form}
    return render(request, 'portfolio/new_workshop.html', context)

@login_required
def edit_workshop_view(request, workshop_id):

    workshop = Workshop.objects.get(id = workshop_id)
    
    if request.POST:
        form = WorkshopForm(request.POST or None, request.FILES, instance=workshop)
        if form.is_valid():
            form.save()
            return redirect('portfolio:workshop', workshop_id = workshop.id)
    else:
        form = WorkshopForm(instance=workshop)
        
    context = {'form': form, 'workshop':workshop}
    return render(request, 'portfolio/edit_workshop.html', context)

@login_required
def delete_workshop_view(request, workshop_id):

    workshop = Workshop.objects.get(id = workshop_id)
    workshop.delete()
    return redirect('portfolio:educations')

# UC views

def uc_view(request, uc_id):

    context = {
        'uc': UC.objects.get(id = uc_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/uc.html', context)

@login_required
def new_uc_view(request):

    form = UCForm(request.POST or None, request.FILES)
    if form.is_valid():
        uc = form.save()
        return redirect('portfolio:course', course_id = uc.course.id)
    
    context = {'form': form}
    return render(request, 'portfolio/new_uc.html', context)

@login_required
def edit_uc_view(request, uc_id):

    uc = UC.objects.get(id = uc_id)
    
    if request.POST:
        form = UCForm(request.POST or None, request.FILES, instance=uc)
        if form.is_valid():
            form.save()
            return redirect('portfolio:uc', uc_id = uc.id)
    else:
        form = UCForm(instance=uc)
        
    context = {'form': form, 'uc':uc}
    return render(request, 'portfolio/edit_uc.html', context)

@login_required
def delete_uc_view(request, uc_id):

    uc = UC.objects.get(id = uc_id)
    course_id = uc.course.id
    uc.delete()
    return redirect('portfolio:course', course_id = course_id)