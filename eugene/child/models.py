from django.db import models


class Child(models.Model):
    name = models.CharField(verbose_name='Имя крошки', max_length=64, blank=True)
    birthday = models.DateField(verbose_name='дата рождения')

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(verbose_name='название фотографии', max_length=100, default='Мимими')
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='child/photo')
    description = models.TextField(verbose_name='описание фотографии')
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)

    def __str__(self):
        return self.title

