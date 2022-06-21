from . import views
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from .views import contact, ContactViewSet

router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', contact),
    path('api/', include(router.urls)),
]
