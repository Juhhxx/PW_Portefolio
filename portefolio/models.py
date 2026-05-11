from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Knowledge level choices and list
NONAPPLICABLE = 0
BEGGINER = 1
INTERMEDIATE = 2
ADVANCED = 3

LEVELS = [
    (NONAPPLICABLE, 'Non Applicable'),
    (BEGGINER, 'Beginner'),
    (INTERMEDIATE, 'Intermediate'),
    (ADVANCED, 'Advanced')
]

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    about = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=' ')
    
    logo = models.ImageField(upload_to='technology_logos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    
    annotations = models.TextField(blank=True, null=True)

    level = models.IntegerField(choices=LEVELS, default=BEGGINER)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='institution_logos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class School(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='schools')

    def __str__(self):
        return self.name

class Education(models.Model):
    from_year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)], default=2025)
    to_year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)], default=2025)

    class Meta:
        abstract = True

class Course(Education):
    name = models.CharField(max_length=100)
    description = models.TextField(default=' ')
    requirements = models.TextField(default=' ')
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    flyer = models.URLField(blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name
    
class Certification(Education):
    name = models.CharField(max_length=100)
    description = models.TextField()
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, related_name='certifications')
    
    link = models.URLField(blank=True, null=True)
    certificate = models.ImageField(upload_to='certifications/', blank=True, null=True)
    
    technologies = models.ManyToManyField(Technology, related_name='certifications', blank=True)

    def __str__(self):
        return self.name

class Workshop(Education):
    name = models.CharField(max_length=100)
    description = models.TextField()
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, related_name='workshops')
    
    link = models.URLField(blank=True, null=True)
    
    technologies = models.ManyToManyField(Technology, related_name='workshops', blank=True)

    def __str__(self):
        return self.name
    
class UC(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)
    description = models.TextField(default=' ')
    program = models.TextField(default=' ')
    objectives = models.TextField(default=' ')
    
    teachers = models.ManyToManyField(Teacher, related_name='ucs', blank=True)

    technologies = models.ManyToManyField(Technology, related_name='ucs', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ucs')
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
    image = models.URLField(blank=True, null=True)
    pdf = models.URLField(blank=True, null=True)
    
    technologies = models.ManyToManyField(Technology, related_name='tfcs')
    
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.IntegerField(choices=LEVELS, default=BEGGINER)
    
    technologies = models.ManyToManyField(Technology, related_name='skills', blank=True)
    projects = models.ManyToManyField(Project, related_name='skills', blank=True)
    tfcs = models.ManyToManyField(TFC, related_name='skills', blank=True)


    def __str__(self):
        return self.name