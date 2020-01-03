from django.shortcuts import render
from sample.models import MainList, SubList
from .serializers import MainListSerializer, SubListSerializer
from rest_framework import viewsets


class MainListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MainList.objects.all()
    serializer_class = MainListSerializer


class SubListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubList.objects.all()
    serializer_class = SubListSerializer
