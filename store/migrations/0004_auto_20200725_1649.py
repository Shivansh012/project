

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200725_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='area',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Area of Box', max_digits=24),
        ),
        migrations.AlterField(
            model_name='box',
            name='volume',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Volume of Box', max_digits=24),
        ),
    ]
