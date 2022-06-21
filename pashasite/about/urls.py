from . import views
from .views import about, AboutViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'about', AboutViewSet)


urlpatterns = [
    path('', about),
    path('api/', include(router.urls)),
]
