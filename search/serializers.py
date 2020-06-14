from rest_framework import serializers
from home.models import food,restro
import django_filters as filters

from rest_framework.generics import ListAPIView

class Foodserializers(serializers.ModelSerializer):
    class Meta:
        model=food
        fields=['restroname','foodname']

class Searchserializers(filters.FilterSet):
    foodname=filters.CharFilter(lookup_expr='icontains')
    #restroname=filters.ModelMultipleChoiceFilter(name='restroname')

    class Meta:
        model=food
        fields=('restroname','foodname')

def compare(list1,list2):
    common=[]
    for i in list1:
        for j in list2:
            if i==j:
                common.append(i)
    common=list(set(common))
    return common




