import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

def run():
    from portefolio.models import Course
    print(Course.objects.count())

if __name__ == "__main__":
    run()