from django.shortcuts import render

from .models import Child


# Create your views here.


def main(request):
    children = Child.objects.all()
    print(children)

    template = 'child/index.html'
    context = {'children': children}

    return render(request, template, context)
