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

def projects_view(request):

    context = {
        'projects': Project.objects.all(),
        'TFCs': TFC.objects.all(),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/projects.html', context)

def skills_view(request):

    context = {
        'skills': Skill.objects.all(),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/skills.html', context)

def makingof_view(request):

    return render(request, 'portfolio/makingof.html')

# Course views

def course_view(request, course_id):

    course = Course.objects.get(id = course_id)
    ucs = course.ucs.all().order_by('year', 'semester')

    context = { 
        'course': course,
        'ucs': ucs,
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

# Teacher views

def teacher_view(request, teacher_id):

    context = {
        'teacher': Teacher.objects.get(id = teacher_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/teacher.html', context)

@login_required
def new_teacher_uc_view(request, uc_id):

    form = TeacherForm(request.POST or None, request.FILES)
    if form.is_valid():
        teacher = form.save()
        uc = UC.objects.get(id=uc_id)
        uc.teachers.add(teacher)
        return redirect('portfolio:uc', uc_id = uc_id)
    
    context = {'form': form}
    return render(request, 'portfolio/new_teacher.html', context)

@login_required
def new_teacher_tfc_view(request, tfc_id):

    form = TeacherForm(request.POST or None, request.FILES)
    if form.is_valid():
        teacher = form.save()
        tfc = TFC.objects.get(id=tfc_id)
        tfc.supervisors.add(teacher)
        return redirect('portfolio:tfc', tfc_id = tfc_id)
    
    context = {'form': form}
    return render(request, 'portfolio/new_teacher.html', context)

@login_required
def edit_teacher_view(request, teacher_id):

    teacher = Teacher.objects.get(id = teacher_id)
    
    if request.POST:
        form = TeacherForm(request.POST or None, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('portfolio:teacher', teacher_id = teacher.id)
    else:
        form = TeacherForm(instance=teacher)
        
    context = {'form': form, 'teacher':teacher}
    return render(request, 'portfolio/edit_teacher.html', context)

@login_required
def delete_teacher_view(request, teacher_id):

    teacher = Teacher.objects.get(id = teacher_id)
    teacher.delete()
    return redirect('portfolio:educations')

@login_required
def delete_teacher_course_view(request, teacher_id, course_id):

    teacher = Teacher.objects.get(id = teacher_id)
    teacher.delete()
    return redirect('portfolio:course', course_id = course_id)

@login_required
def delete_teacher_tfc_view(request, teacher_id, tfc_id):

    teacher = Teacher.objects.get(id = teacher_id)
    teacher.delete()
    return redirect('portfolio:tfc', tfc_id = tfc_id)

# Project views

def project_view(request, project_id):

    context = {
        'project': Project.objects.get(id = project_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/project.html', context)

@login_required
def new_project_view(request):

    form = ProjectForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projects')
    
    context = {'form': form}
    return render(request, 'portfolio/new_project.html', context)

@login_required
def new_project_skill_view(request, skill_id):

    form = ProjectForm(request.POST or None, request.FILES)
    if form.is_valid():
        project = form.save()
        skill = Skill.objects.get(id = skill_id)
        skill.projects.add(skill)
        return redirect('portfolio:skill', skill_id = skill_id)
    
    context = {'form': form}
    return render(request, 'portfolio/new_project.html', context)

@login_required
def edit_project_view(request, project_id):

    project = Project.objects.get(id = project_id)
    
    if request.POST:
        form = ProjectForm(request.POST or None, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio:project', project_id = project.id)
    else:
        form = ProjectForm(instance=project)
        
    context = {'form': form, 'project':project}
    return render(request, 'portfolio/edit_project.html', context)

@login_required
def delete_project_view(request, project_id):

    project = Project.objects.get(id = project_id)
    project.delete()
    return redirect('portfolio:projects')

# TFC views

def tfc_view(request, tfc_id):

    context = {
        'tfc': TFC.objects.get(id = tfc_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/tfc.html', context)

@login_required
def new_tfc_view(request):

    form = TFCForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portfolio:skill', skill_id = skill_id)
    
    context = {'form': form}
    return render(request, 'portfolio/new_tfc.html', context)

@login_required
def new_tfc_skill_view(request, skill_id):

    form = TFCForm(request.POST or None, request.FILES)
    if form.is_valid():
        tfc = form.save()
        skill = Skill.objects.get(id = skill_id)
        skill.tfcs.add(tfc)
        return redirect('portfolio:tfcs')
    
    context = {'form': form}
    return render(request, 'portfolio/new_tfc.html', context)

@login_required
def edit_tfc_view(request, tfc_id):

    tfc = TFC.objects.get(id = tfc_id)
    
    if request.POST:
        form = TFCForm(request.POST or None, request.FILES, instance=tfc)
        if form.is_valid():
            form.save()
            return redirect('portfolio:tfc', tfc_id = tfc.id)
    else:
        form = TFCForm(instance=tfc)
        
    context = {'form': form, 'tfc':tfc}
    return render(request, 'portfolio/edit_tfc.html', context)

@login_required
def delete_tfc_view(request, tfc_id):

    tfc = TFC.objects.get(id = tfc_id)
    tfc.delete()
    return redirect('portfolio:projects')

# Technology views

def technology_view(request, technology_id):

    context = {
        'technology': Technology.objects.get(id = technology_id),
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/technology.html', context)

@login_required
def new_technology_project_view(request, project_id):

    form = TechnologyForm(request.POST or None, request.FILES)
    if form.is_valid():
        technology = form.save()
        project = Project.objects.get(id = project_id)
        project.technologies.add(technology)
        return redirect('portfolio:project', project_id = project_id)
    
    context = {'form': form}
    return render(request, 'portfolio/new_technology.html', context)

@login_required
def new_technology_tfc_view(request, tfc_id):

    form = TechnologyForm(request.POST or None, request.FILES)
    if form.is_valid():
        technology = form.save()
        tfc = TFC.objects.get(id = tfc_id)
        tfc.technologies.add(technology)
        return redirect('portfolio:tfc', tfc_id = tfc_id)
    
    context = {'form': form}
    return render(request, 'portfolio/new_technology.html', context)

@login_required
def edit_technology_view(request, technology_id):

    technology = Technology.objects.get(id = technology_id)
    
    if request.POST:
        form = TechnologyForm(request.POST or None, request.FILES, instance=technology)
        if form.is_valid():
            form.save()
            return redirect('portfolio:technology', technology_id = technology.id)
    else:
        form = TechnologyForm(instance=technology)
        
    context = {'form': form, 'technology':technology}
    return render(request, 'portfolio/edit_technology.html', context)

@login_required
def delete_technology_view(request, technology_id):

    technology = Technology.objects.get(id = technology_id)
    technology.delete()
    return redirect('portfolio:projects')

@login_required
def delete_technology_project_view(request, technology_id, project_id):

    technology = Technology.objects.get(id = technology_id)
    technology.delete()
    return redirect('portfolio:project', project_id = project_id)

@login_required
def delete_technology_tfc_view(request, technology_id, tfc_id):

    technology = Technology.objects.get(id = technology_id)
    technology.delete()
    return redirect('portfolio:tfc', tfc_id = tfc_id)

# Skill views

def skill_view(request, skill_id):

    skill = Skill.objects.get(id = skill_id)

    context = { 
        'skill': skill,
        'gestor': request.user.groups.filter(name='gestor_portefolio').exists(),
    }

    return render(request, 'portfolio/skill.html', context)

@login_required
def new_skill_view(request):

    form = SkillForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('portfolio:educations')
    
    context = {'form': form}
    return render(request, 'portfolio/new_skill.html', context)

@login_required
def edit_skill_view(request, skill_id):

    skill = Skill.objects.get(id = skill_id)
    
    if request.POST:
        form = SkillForm(request.POST or None, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('portfolio:skill', skill_id = skill.id)
    else:
        form = SkillForm(instance=skill)
        
    context = {'form': form, 'skill':skill}
    return render(request, 'portfolio/edit_skill.html', context)

@login_required
def delete_skill_view(request, skill_id):

    skill = Skill.objects.get(id = skill_id)
    skill.delete()
    return redirect('portfolio:skills')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             