# Generated by Django 2.0.1 on 2018-12-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='child/photo'),
        ),
    ]
