from django.contrib import admin

# Register your models here.

from .models import Child, Photo

admin.site.register(Child)
admin.site.register(Photo)


