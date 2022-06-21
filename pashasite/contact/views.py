from django.shortcuts import render
from rest_framework import viewsets

from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail

from .serializers import ContactSerializer


def contact(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                send_mail(form.cleaned_data['name'], form.cleaned_data['contact'],
                          form.cleaned_data['message'], 'alexeyrachuk94@gmail.com', ['alexeyrachuk94@gmail.com'],
                          fail_silently=False)
            except:
                error = 'Форма не была отправлена'
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'error': error, 'contacts': Contact.objects.all()})


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
