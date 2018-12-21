from django.shortcuts import render, get_object_or_404

from . import models
from .models import Child, Photo


# Create your views here.


def main(request):
    children = Child.objects.all()
    print(children)

    template = 'child/index.html'
    context = {'children': children}

    return render(request, template, context)


def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def child(request, pk=None):
    child_obj = get_object_or_404(models.Child, pk=pk)
    photos = child_obj.photo_set.all()
    rows_of_photos = chunk_data(photos, 5)
    template = 'child/child_page.html'
    context = {'child': child_obj, 'photos': photos,
               'rows_of_photos': rows_of_photos}
    return render(request, template, context)


def photo(request, pk=None):
    photo_obj = get_object_or_404(models.Photo, pk=pk)
    template = 'child/photo_page.html'
    context = {'photo': photo_obj}
    return render(request, template, context)


def family(request):
    pass


   # def photos(request, pk=None):
    #    child_obj = get_object_or_404(models.Child, pk=pk)
    #    photos = child_obj.photo_set.all()
    #    rows_of_products = chunk_data(photos, 4)
    #    template = 'child/child_page.html'
    #    context = {'photos': photos,
    #               'rows_of_products': rows_of_products,
     #              }
     #   return render(request, template, context)




