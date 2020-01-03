from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from sample.models import MainList, SubList
from .serializers import MainListSerializer, SubListSerializer
from rest_framework import viewsets


class MainListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MainList.objects.all()
    serializer_class = MainListSerializer
    permission_classes = [IsAuthenticated]  # 認証済みのみアクセス可能


class SubListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubList.objects.all()
    serializer_class = SubListSerializer
    permission_classes = [IsAuthenticated]  # 認証済みのみアクセス可能
