# Generated by Django 4.0.4 on 2022-12-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_postulacion_reporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulacion',
            name='imagen',
            field=models.ImageField(null=True, upload_to='postulaciones'),
        ),
        migrations.AddField(
            model_name='reporte',
            name='imagen',
            field=models.ImageField(null=True, upload_to='reportes'),
        ),
    ]
