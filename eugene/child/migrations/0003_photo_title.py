# Generated by Django 2.0.1 on 2018-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0002_auto_20181209_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='Мимими', max_length=100, verbose_name='название фотографии'),
        ),
    ]