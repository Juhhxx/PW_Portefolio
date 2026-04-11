from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Knowledge level choices and list
BEGGINER = 1
INTERMEDIATE = 2
ADVANCED = 3

LEVELS = [
    (BEGGINER, 'Beginner'),
    (INTERMEDIATE, 'Intermediate'),
    (ADVANCED, 'Advanced')
]

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)
    about = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    logo = models.ImageField(upload_to='technology_logos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    
    annotations = models.TextField(blank=True, null=True)

    level = models.IntegerField(choices=LEVELS, default=BEGGINER)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    flyer = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class UC(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    program = models.TextField()
    objectives = models.TextField()
    
    teachers = models.ManyToManyField(Teacher, related_name='ucs')

    technologies = models.ManyToManyField(Technology, related_name='ucs', blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name='ucs')
    image = models.ImageField(upload_to='uc_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    uc = models.ForeignKey(UC, on_delete=models.CASCADE, related_name='projects')
    applied_concepts = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects')
    
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    repository = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class TFC(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField(validators=[MinValueValidator(2020), MaxValueValidator(2030)])
    
    supervisors = models.ManyToManyField(Teacher, related_name='tfcs')
    courses = models.ManyToManyField(Course, related_name='tfcs')
    
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='tfc_images/', blank=True, null=True)
    pdf = models.URLField(blank=True, null=True)
    
    technologies = models.ManyToManyField(Technology, related_name='tfcs')
    
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)

    def __str__(self):
        return self.name