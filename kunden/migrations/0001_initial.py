from django.contrib.auth import get_user_model
from django.db import migrations

def create_superuser(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            'admin', 'philip.pointecker@gmail.com', 'po'
        )

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(...),  # hier sind die normalen Model-Operationen
        migrations.RunPython(create_superuser),  # <--- das hier fügst du dazu
    ]
