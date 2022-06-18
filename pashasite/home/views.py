from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Home, Works, ImageSet


class WorkSingle(DetailView):
    model = Works
    slug_field = 'url'
    template_name = 'home/single-page.html'
    context_object_name = 'single'


class ImageSets(DetailView):
    model = ImageSet
    context_object_name = 'image'


def home(request):
    return render(request, 'home/index.html', {'homes': Home.objects.all(),
                                               'works': Works.objects.all().filter(draft=True).order_by(
                                                   '-date'),
                                               'images': ImageSet.objects.all().order_by('order')})
