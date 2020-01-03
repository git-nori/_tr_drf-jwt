from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('mainlist', views.MainListViewSet)
router.register('sublist', views.SubListViewSet)

urlpatterns = [
    path('', include(router.urls))
]
