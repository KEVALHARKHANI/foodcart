from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import auth
from .models import restro,food,cart,address
from history.models import Histroy
from django.contrib import messages
from history.mixin import objectviewmixin
from django.views.generic import ListView,DetailView


from .ahm_pincode import pincode
# Create your views here.
def history(user,id):
    data=Histroy.objects.filter(user_id=user,object_id_id=id)
    print(data)
    if len(data)==0:
        save_data = Histroy(user_id=user, object_id_id=id, click=1,preferred=0)
        save_data.save()
    else:
        for i in data:
            click=1+i.click
            pk=i.id
        save_data = Histroy(id=pk,user_id=user, object_id_id=id, click=click,preferred=0)
        save_data.save()

def home(request):
    if request.user.is_authenticated:
        request.session['refresh'] = False
        if request.user.is_authenticated:
            request.session['refresh'] = True
        history=Histroy.objects.filter(user_id=request.user.id).order_by('-click')
        if len(history)!=0:
            return render(request, 'index.html', {'most_viewed': history})
        else:
            rest = restro.objects.all()
            return render(request, 'index.html', {'rest': rest})
    else:
        rest = restro.objects.all()
        return render(request, 'index.html', {'rest': rest})

def foods(request,restroid):
    if request.user.is_authenticated:
        if request.session['refresh']==True:
            history(request.user.id,restroid)
            request.session['refresh']=False
            print('yes')

        fooddetail=food.objects.filter(restroname_id=restroid)
        if len(fooddetail)!=0:
            return render(request,'food.html',{'food':fooddetail})
        else:
            messages.info(request,'parameter error')
            return redirect('/')
    else:
        messages.info(request,'please...login')
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('home')
def order(request):
    return redirect('/myaccount')





