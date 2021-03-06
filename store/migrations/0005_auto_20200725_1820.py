

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200725_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='area',
            field=models.IntegerField(default=0, help_text='Area of Box'),
        ),
        migrations.AlterField(
            model_name='box',
            name='height',
            field=models.IntegerField(default=0, help_text='Height of Box'),
        ),
        migrations.AlterField(
            model_name='box',
            name='length',
            field=models.IntegerField(default=0, help_text='Length of Box'),
        ),
        migrations.AlterField(
            model_name='box',
            name='volume',
            field=models.IntegerField(default=0, help_text='Volume of Box'),
        ),
        migrations.AlterField(
            model_name='box',
            name='width',
            field=models.IntegerField(default=0, help_text='Width of Box'),
        ),
    ]
