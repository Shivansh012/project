

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='area',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Area of Box', max_digits=8),
        ),
        migrations.AddField(
            model_name='box',
            name='volume',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Volume of Box', max_digits=8),
        ),
        migrations.AlterField(
            model_name='box',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Height of Box', max_digits=8),
        ),
        migrations.AlterField(
            model_name='box',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Length of Box', max_digits=8),
        ),
        migrations.AlterField(
            model_name='box',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Width of Box', max_digits=8),
        ),
    ]
