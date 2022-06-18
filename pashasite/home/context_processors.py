from .models import Home


def copywrite_get(request):
    copywrite = Home.objects.get(id=1)
    return {'copywrite': copywrite}
