from django.contrib.auth import get_user_model

from django.db import migrations
import os


def createdefaultuser(apps, schema_editor):
    admin_password = os.environ["ADMIN_PASSWORD"]
    User = get_user_model()
    User.objects.create_superuser(os.environ["ADMIN_ACCOUNT"], password=admin_password)


class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [migrations.RunPython(createdefaultuser)]
