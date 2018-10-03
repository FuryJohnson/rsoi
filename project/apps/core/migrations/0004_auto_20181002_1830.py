# Generated by Django 2.1.1 on 2018-10-02 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181002_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.University'),
        ),
    ]
