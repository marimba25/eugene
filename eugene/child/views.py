from django.shortcuts import render, get_object_or_404

from . import models
from .models import Child, Photo


# Create your views here.


def main(request):
    children = Child.objects.all()
    albums = []
    for child in children:
        photo = child.photo_set.first()
        albums.append({'child': child, 'photo': photo})
    print(albums)

    template = 'child/index.html'
    context = {'albums': albums}

    return render(request, template, context)


def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def child(request, pk=None):
    child_obj = get_object_or_404(models.Child, pk=pk)
    photos = child_obj.photo_set.all().order_by('date')

    template = 'child/child_page.html'
    context = {'child': child_obj, 'photos': photos}
    return render(request, template, context)


def photo(request, pk=None):

    photo_obj = get_object_or_404(models.Photo, pk=pk)
    child_obj = photo_obj.child
    template = 'child/photo_page.html'
    context = {'photo': photo_obj, 'child': child_obj}
    return render(request, template, context)


def family(request, pk=None):
    child_obj = get_object_or_404(models.Child, pk=pk)
    family_set = child_obj.familymember_set.all()
    print(family_set)
    template = 'child/family.html'
    context = {'family': family_set, 'child': child_obj}
    return render(request, template, context)






