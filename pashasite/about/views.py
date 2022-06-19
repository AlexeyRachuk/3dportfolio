from django.shortcuts import render

from .models import About


def about(request):
    return render(request, 'about/about.html', {'abouts': About.objects.all()})
