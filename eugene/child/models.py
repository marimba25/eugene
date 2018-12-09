from django.db import models

# Create your models here.


class Child(models.Model):
    name = models.CharField(verbose_name='Имя крошки', max_length=64, blank=True)
    birthday = models.DateField(verbose_name='дата рождения')

    def __str__(self):
        return self.name


class Photo(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='child/photo')
    description = models.TextField(verbose_name='описание фотографии')
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)



# '/home/marina/PycharmProjects/eugene/eugene/child/photo/mimi.jpg'