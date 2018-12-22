from django.db import models


class Child(models.Model):
    SEX = ((1, 'Мальчик'),
            (2, 'Девочка'))
    name = models.CharField(verbose_name='Имя крошки', max_length=64, blank=True)
    birthday = models.DateField(verbose_name='дата рождения')
    sex = models.IntegerField(choices=SEX, verbose_name='Пол', null=True, blank=True)

    def __str__(self):
        return self.name or "No name"


class Photo(models.Model):
    title = models.CharField(verbose_name='название фотографии', max_length=100, blank=True)
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='child/photo')
    description = models.TextField(verbose_name='описание фотографии', blank=True)
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)

    def __str__(self):
        return self.title or 'No title'


class FamilyMember(models.Model):
    name = models.CharField(verbose_name='Имя родственника', max_length=100, default="Родственник")
    relationship = models.CharField(verbose_name='Отношение', max_length=100)
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='child/photo', blank=True)

    def __str__(self):
        return self.name

