from django.shortcuts import render
from rest_framework import viewsets

from .models import About
from .serializers import AboutSerializer


def about(request):
    return render(request, 'about/about.html', {'abouts': About.objects.all()})


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
