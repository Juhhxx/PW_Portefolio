import os
import django

# configure settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# initialize django
django.setup()

from django.conf import settings
from django.core.files import File
from portefolio.models import Technology

def run():
    for obj in Technology.objects.all():
        if obj.logo and obj.logo.name:   # adaptar o nome do campo (neste caso é "logom")
            local_path = os.path.join(
                settings.MEDIA_ROOT,
                obj.logo.name
            )

            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.logo.save(                         # adequar
                        os.path.basename(local_path),
                        File(f),
                        save=True
                    )
                print(f"Migrado: {obj}")

if __name__ == "__main__":
    run()