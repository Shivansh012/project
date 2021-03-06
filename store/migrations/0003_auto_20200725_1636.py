

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200725_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='created_by',
            field=models.ForeignKey(help_text='User Created', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
