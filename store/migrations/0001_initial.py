

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, help_text='Length of Box', max_digits=8)),
                ('width', models.DecimalField(decimal_places=2, help_text='Width of Box', max_digits=8)),
                ('height', models.DecimalField(decimal_places=2, help_text='Height of Box', max_digits=8)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.OneToOneField(help_text='User Created', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
