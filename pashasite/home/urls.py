from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home),
    path("<slug:slug>/", views.WorkSingle.as_view(), name="single"),

]
