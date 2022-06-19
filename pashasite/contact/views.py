from django.shortcuts import render

from .models import Contact


def contact(request):
    return render(request, 'contact/contact.html', {'contacts': Contact.objects.all()})
