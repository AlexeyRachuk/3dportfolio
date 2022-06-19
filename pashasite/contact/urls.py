from . import views
from django.urls import path

from .views import contact

urlpatterns = [
    path('', contact),
]