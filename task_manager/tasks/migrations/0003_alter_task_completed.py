# Generated by Django 5.1 on 2024-09-04 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.CharField(choices=[('doing', 'Doing'), ('done', 'Done')], max_length=5),
        ),
    ]
