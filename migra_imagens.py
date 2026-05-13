import os
from django.core.files import File
from portefolio.models import Teacher

def run():
    for obj in Teacher.objects.all():
        if obj.photo and obj.photo.name:   # adaptar o nome do campo (neste caso é "imagem")
            local_path = obj.photo.path    # adequar

            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    obj.photo.save(                         # adequar
                        os.path.basename(local_path),
                        File(f),
                        save=True
                    )
                print(f"Migrado: {obj}")

if __name__ == "__main__":
    run()