import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

def get_tfc_data() -> list:
    tfc_data = os.path.join(os.getcwd(), 'data', 'dados_tfcs.json')
    
    with open(tfc_data, 'r', encoding="utf8") as f:
        data = json.load(f)
        return data

def create_tfc(tfc_info: dict):
    from portefolio.models import TFC, Teacher, Course, Technology, School
    
    if TFC.objects.filter(name=tfc_info['Titulo']).exists():
        return

    tfc = TFC.objects.create(
        name=tfc_info['Titulo'],
        description=tfc_info['Sumario'],
        year=tfc_info['Ano'],
        image=tfc_info.get('Imagem'),
        pdf=tfc_info.get('Link_PDF')
    )
    
    for teacher_name in tfc_info['Orientadores']:
        if Teacher.objects.filter(name=teacher_name).exists():
            teacher = Teacher.objects.get(name=teacher_name)
        else:
            teacher = Teacher.objects.create(name=teacher_name)
            
        tfc.supervisors.add(teacher)
    
    for course_name in tfc_info['Licenciaturas']:
        if Course.objects.filter(name=course_name).exists():
            course = Course.objects.get(name=course_name)
        else:
            course = Course.objects.create(name=course_name, school=School.objects.get(acronym='ECATI'))
            
        tfc.courses.add(course)
    
    for tech_name in tfc_info['Tecnologias_Usadas']:
        if Technology.objects.filter(name=tech_name).exists():
            technology = Technology.objects.get(name=tech_name)
        else:
            technology = Technology.objects.create(name=tech_name)
            
        tfc.technologies.add(technology)
    
    tfc.save()
        
    return tfc

def run():
    tfcs = get_tfc_data()
    
    for tfc_info in tfcs:
        create_tfc(tfc_info)
        print(f"TFC '{tfc_info['Titulo']}' created successfully.")

if __name__ == "__main__":
    run()