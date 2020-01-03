from rest_framework import serializers
from sample.models import MainList, SubList


class MainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainList
        fields = ('title', 'datetime')


class SubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubList
        fields = ('title', 'totalnum')
