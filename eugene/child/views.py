from django.shortcuts import render, get_object_or_404

from . import models
from .models import Child


# Create your views here.


def main(request):
    children = Child.objects.all()
    print(children)

    template = 'child/index.html'
    context = {'children': children}

    return render(request, template, context)


def child(request, pk=None):
    child_obj = get_object_or_404(models.Child, pk=pk)
    photos = child_obj.photo_set.all()
    template = 'child/child_page.html'
    context = {'child': child_obj, 'photos': photos}
    return render(request, template, context)




