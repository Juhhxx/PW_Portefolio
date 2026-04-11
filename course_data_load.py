import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

def get_uc_data() -> list:
    uc_data = os.path.join(os.getcwd(), 'data', 'dados_ucs.json')
    
    with open(uc_data, 'r', encoding="utf8") as f:
        data = json.load(f)
        return data

def create_uc(uc_info: dict):
    from portefolio.models import UC, Course
    
    if UC.objects.filter(name=uc_info['curricularUnitName']).exists():
        return
    
    uc = UC.objects.create(
        name=uc_info.get('curricularUnitName', ''),
        description=uc_info.get('presentation', ''),
        program=uc_info.get('programme', ''),
        objectives=uc_info.get('objectives', '')
    )
    
    uc.courses.add(Course.objects.get(name=uc_info['courseName']))
    
    uc.save()

    return uc 

def run():
    ucs_info = get_uc_data()
    
    for uc in ucs_info[0]['ucList']:
        create_uc(uc)
        print(f"UC '{uc['curricularUnitName']}' created successfully.")

if __name__ == "__main__":
    run()