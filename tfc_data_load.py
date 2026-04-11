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

def run():
    tfcs = get_tfc_data()
    print(f"Total TFCs: {len(tfcs)}")

if __name__ == "__main__":
    run()