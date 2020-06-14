from django.shortcuts import render,redirect,HttpResponse
from home.models import cart, address, food
from django.contrib import messages
from home.ahm_pincode import pincode
from .models import Card
from myaccount.models import Orders
# Create your views here.

def cart1(request):
    uid=request.user.id
    cart_data=cart.objects.filter(username_id=uid).order_by('id')
    if len(cart_data)==0:

        return render(request,'cart.html',{'message':'your cart is empty'})
    else:
        total=0;
        discount=0
        for i in cart_data:
            total=total+(i.quantity*i.foodname.price)
            if i.restroname.specialoffer:
                discount=int(i.restroname.offer)
        request.session['discount'] =(total*discount)/100
        request.session['food'] = total
        request.session['total']=total+50-int((total*discount)/100)
        return render(request,'cart.html',{'cdata':cart_data})

def add_to_cart(request):
    food_id = request.GET['id']
    cu = request.user
    alldata=cart.objects.filter(username_id=cu.id)
    rdata = food.objects.filter(id=food_id)
    for i in rdata:
        restoid = i.restroname_id
    if len(alldata)==0:
        data = cart(quantity=1, foodname_id=food_id, username_id=cu.id,restroname_id=restoid)
        data.save()
        return HttpResponse('food added successfully')
    else:
        fdata=cart.objects.filter(foodname_id=food_id,username_id=cu.id)

        if len(fdata)==0:
            for m in alldata:
                rid=m.restroname_id
            if rid==restoid:
                data = cart(quantity=1, foodname_id=food_id, username_id=cu.id,restroname_id=rid)
                data.save()
                return HttpResponse('food added successfully')
            else:
                return HttpResponse("you can't add food from another restaurant" )
        else:
            for i in fdata:
                quantity=i.quantity+1
                i.quantity=quantity
                i.save()
                return HttpResponse('food added successfully')
def fdelete(request):
    fid=request.GET['fid']
    cu=request.user
    data = cart.objects.filter( foodname_id=fid, username_id=cu.id)
    for i in data:
        uquantiy=i.quantity
    if uquantiy!=1:
        i.quantity=int(uquantiy)-1
        i.save()
    else:
        i.delete()
    return redirect('cart')
def fadd(request):
    fid=request.GET['fid']
    cu=request.user
    data = cart.objects.filter( foodname_id=fid, username_id=cu.id)
    for i in data:
        uquantiy=i.quantity
    i.quantity=int(uquantiy)+1
    i.save()
    return redirect('cart')
def remove(request):
    fid=request.GET['fid']
    cu=request.user
    data = cart.objects.filter(foodname_id=fid, username_id=cu.id)
    for i in data:
        i.delete()
    return redirect('cart')
def new_address(request):
    return render(request,'newaddress.html')
def add_address(request):
    uid=request.user.id
    name=request.POST['name']
    phone=request.POST['phone']
    pincode=request.POST['pincode']
    maddress=request.POST['address']
    landmark=request.POST['landmark']
    area=request.POST['area']
    city=str(area)+','+'ahemdabad'
    save_address=address(name=name,phone=phone,pincode=pincode,city=city,house=maddress,location=landmark,username_id=uid)
    save_address.save()
    return redirect('procced')

def zipcode(request):
    id=request.GET['code']
    code=pincode()
    try:
        flage=code[id]
    except:
        flage="no"
    return HttpResponse(flage)
def check_address(request):
    uid=request.user
    address_data = address.objects.filter(username_id=uid.id)
    if len(address_data) == 0:
        messages.info(request, 'no address found please add new address')
        return redirect('naddress')

    else:
         return render(request,'order_address.html',{'data':address_data})
def select_address(request):
    id=request.GET['id']
    request.session['address_id']=id
    return redirect('checkout')
def checkout(request):
    if request.session['address_id']:
        id=request.session['address_id']
    else:
        messages.info(request,'please select address')
        return redirect('select_address')
    address_data=address.objects.filter(id=id)
    cart_data=cart.objects.filter(username_id=request.user.id)
    return render(request,'checkout.html',{'adata':address_data,'cdata':cart_data})
def payment(request):
    data=Card.objects.filter(username_id=request.user.id)
    return render(request,'payment.html',{'card_data':data})

def add_to_card(request):
    name=request.GET['name']
    card_number=request.GET['number']
    expiry=request.GET['date']
    card_data=Card(name=name,card_number=card_number,expiry_date=expiry,username_id=request.user.id)
    card_data.save()
    return redirect('payment')
def payment_method(request):
    foods_id=''
    quantity=''
    name=request.POST['payment']
    if name=="netbanking":
        bank=request.POST['bank']
        payment_data=str(name)+"&"+str(bank)
    elif name=="upi":
        upi_id=request.POST['id']
        payment_data = str(name) + "&" + str(upi_id)
    elif name=='cod':
        payment_data = str(name) + "&" + str(" ")
    elif 'card' in name:
        payment_data = str(name)
    if payment_data:
        if request.session['address_id']:
            address_data=address.objects.filter(id=request.session['address_id'],username_id=request.user.id)
        else:
            messages.info(request,'please select address')
            return redirect('select_address')
        cart_data=cart.objects.filter(username_id=request.user.id)
        for f in cart_data:
            foods_id=foods_id+str(f.foodname.id)+","
            restroid=f.restroname.id
            quantity = quantity + str(f.quantity) + ","
        if address_data:
            for i in address_data:
                full_address=str(i.name)+'&'+str(i.phone)+'&'+str(i.pincode)+'&'+str(i.house)+'&'+str(i.city)+'&'+str(i.location)
            oder_data=Orders(payment_method=payment_data,total=request.session['total'],foodsid=foods_id,address=full_address,restroid_id=restroid,quantity=quantity,username_id=request.user.id)
            oder_data.save()
            cart.objects.filter(username_id=request.user.id).delete()
            messages.info(request,'order placed successfully')
            return redirect('/')
        else:
            messages.info(request,'problem with address')
            return redirect('/')

    else:
        messages.info(request,'something went wrong')
        return redirect('/')
    return redirect('payment')