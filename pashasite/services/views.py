from django.shortcuts import render
from .models import ServicesMain, ServicesBig, ServicesSmall


def services(request):
    return render(request, 'services/services.html', {'services_main': ServicesMain.objects.all(),
                                                      'services_big': ServicesBig.objects.all().filter(
                                                          draft=True).order_by('order'),
                                                      'services_small': ServicesSmall.objects.filter(
                                                          draft=True).order_by('order')})
