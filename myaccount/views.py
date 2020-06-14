from django.shortcuts import render,redirect
from home.models import address,food
from home.ahm_pincode import pincode
from login.models import userdata
from cart.models import Card
from .models import Orders

# Create your views here.
def myaccount(request):
    return render(request,'myaccount.html')

def view_address(request):
    address_data=address.objects.filter(username_id=request.user.id)
    return render(request,'order_address.html',{'data':address_data})
def edit_address(request,id):
    address_data=address.objects.filter(id=id)
    for i in address_data:
        pin=i.pincode
    area=pincode()
    return render(request,'newaddress.html',{'edit':True,'adata':address_data,'area':area[str(pin)]})
def edit_add_address(request):
    id=request.GET['id']
    uid=request.user.id
    name=request.POST['name']
    phone=request.POST['phone']
    pincode=request.POST['pincode']
    maddress=request.POST['address']
    landmark=request.POST['landmark']
    area=request.POST['area']
    city=str(area)+','+'ahemdabad'
    save_address=address(id=id,name=name,phone=phone,pincode=pincode,city=city,house=maddress,location=landmark,username_id=uid)
    save_address.save()
    return redirect('address')
def delete_address(request,id):
    data=address.objects.filter(id=id)
    data.delete()
    return redirect('address')
def new_address(request):
    return render(request,'newaddress.html')
def  new_add_address(request):
    uid = request.user.id
    name = request.POST['name']
    phone = request.POST['phone']
    pincode = request.POST['pincode']
    maddress = request.POST['address']
    landmark = request.POST['landmark']
    area = request.POST['area']
    city = str(area) + ',' + 'ahemdabad'
    save_address = address(name=name, phone=phone, pincode=pincode, city=city, house=maddress, location=landmark,username_id=uid)
    save_address.save()
    return redirect('address')

def profile(request):
    print(request.user.id)
    user_data=userdata.objects.filter(user_id=request.user.id)
    print(user_data)
    return render(request,'profile.html',{'user_data':user_data})
def saved_card(request):
    cdata=Card.objects.filter(username_id=request.user.id)
    if cdata:
        return render(request,'card.html',{'cdata':cdata})
    else:
        return render(request, 'card.html', {'error':'No saved card available'})
def card_delete(request,id):
    card_data=Card(id=id)
    card_data.delete()
    return redirect('saved_card')
def new_card(request):
    return render(request,'new_card.html')

def add_to_card(request):
    name=request.GET['name']
    card_number=request.GET['number']
    expiry=request.GET['date']
    card_data=Card(name=name,card_number=card_number,expiry_date=expiry,username_id=request.user.id)
    card_data.save()
    return redirect('saved_card')
def order_details(request):
    order_data=Orders.objects.filter(username_id=request.user.id)
    main_data=[]
    if order_data:
        for i in order_data:
            food_id=str(i.foodsid).split(',')
            print(food_id[:-1])
            food_object=food.objects.filter(id__in=food_id[:-1])
            main_data.append([i,food_object])
        print(main_data)
        return render(request, 'order.html', {'order_data':main_data})
    else:
        print("no data")
        return render(request,'order.html',{'error':'no past order'})



