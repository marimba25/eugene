from child.models import Child
from django.shortcuts import render


def users(request):
    title = 'админка/дети'
    children_list = Child.objects.all()
    content = {
        'title': title,
        'objects': children_list
    }
    return render(request, 'adminapp/base.html', content)


