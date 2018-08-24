# Generated by Django 2.0.5 on 2018-08-17 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_p_images_p_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_images',
            name='p_post',
        ),
        migrations.AddField(
            model_name='projects',
            name='feature_images',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.P_Images'),
        ),
    ]