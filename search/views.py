from django.shortcuts import render
from django.db.models import Q
from .serializers import Foodserializers,compare
from home.models import food,restro
from django.contrib import messages
from django.views.generic import ListView
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView


# Create your views here.

class Search_bar(ListView):
    def post(self, request, *args, **kwargs):
        q = str(request.POST['q'])
        query = q
        query_list = q.split(' ')
        food_queryset_list = []
        restro_queryset_list = []
        query_error = []
        for q in query_list:
            food_queryset = list(food.objects.filter(Q(foodname__icontains=q) |
                                                     Q(contain__icontains=q) |
                                                     Q(catagery__icontains=q))
                                 )
            if food_queryset:
                if food_queryset_list and food_queryset:
                    food_queryset_list = compare(food_queryset_list, food_queryset)
                else:
                    food_queryset_list.extend(food_queryset)
            print('food:', food_queryset_list)
            restro_queryset = restro.objects.filter(Q(catagery__icontains=q) |
                                                    Q(detail__icontains=q) |
                                                    Q(restroname__icontains=q) |
                                                    Q(address__icontains=q)
                                                    )
            if restro_queryset:
                if restro_queryset_list and restro_queryset:
                    restro_queryset_list = compare(restro_queryset_list, restro_queryset)
                else:
                    restro_queryset_list.extend(restro_queryset)
                restro_queryset_list.extend(restro_queryset)
            if not food_queryset and not restro_queryset:
                query_error.append(q)
        print('retsro:', restro_queryset_list)
        if food_queryset_list or restro_queryset_list:
            return render(request, 'search_result.html',
                          {'restro': set(restro_queryset_list), 'food': set(food_queryset_list),
                           'query_error': query_error, 'query': query})
        else:
            messages.info(request, 'Product Not found')
            return render(request, 'search_result.html', {'empty_flage': True, 'query': query})





