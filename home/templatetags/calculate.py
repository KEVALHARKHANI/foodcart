from django import template
from django.utils.safestring import mark_safe
register=template.Library()
@register.simple_tag
def multiply(value1,value2,*args,**kwargs):
    return value1*value2
@register.simple_tag
def add(value1,value2,*args,**kwargs):
    return value1+value2
@register.filter
def path(string1):
    string1=str(string1)
    list=string1.split('/')
    track=''
    path=""
    try:
        list1=filter(lambda i:i!="",list)
    except Exception as e:
        print(e)
    for i in list1:
        track=track+"/"+i
        if '_' in i:
            i=i.replace('_',' ')
        path=path+"<a href='"+track+"'>"+i+"</a>/"

    return mark_safe(path)
@register.simple_tag
def date(value1,*args,**kwargs):
    string1=str(value1)
    expiry_date=string1[0:2]+'/'+string1[2:]
    return expiry_date