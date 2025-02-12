from django.shortcuts import render, redirect
from Client.models import ClientDB, BookingDB, OrderDB
from User.models import PostDB
from Admin.models import CategoryDB
from django.contrib import messages
from datetime import datetime


# Create your views here.
def client_index(request):
    cat = CategoryDB.objects.all()
    return render(request, "client_index.html", {'cat':cat})
def register_client(request):
    return render(request, "register_client.html")
def save_client(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('password')
        e = request.POST.get('city')
        f = request.POST.get('address')
        g = request.POST.get('password2')
        obj = ClientDB(Name=a, Email=b, Mobile=c, Password=d, City=e, Address=f)
        obj.save()
        return redirect(register_client)
def client_home(request):
    ads = PostDB.objects.all()
    categories = CategoryDB.objects.all()
    return render(request, "client_home.html", {'ads':ads, 'categories':categories})
def ClientLogin(request):
    return render(request, "client_login.html")
def ClientLoginAuth(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        psw = request.POST.get('pass')
        if ClientDB.objects.filter(Email=un, Password=psw).exists():
            request.session['Email'] = un
            request.session['Password'] = psw
            messages.success(request, "Welcome")
            return redirect(client_home)
        else:
            messages.warning(request, "invalid Password")
            return redirect(ClientLogin)
    else:
        messages.warning(request, "invalid Username")
        return redirect(ClientLogin)
def SingleProduct(request, pro_id):
    data = PostDB.objects.get(id=pro_id)
    categories = CategoryDB.objects.all()
    return render(request, "singleproduct.html", {'data':data})
def aboutUs(req):
    return render(req, "about_us.html")
def booking(req, pro_id):
    current_time = int(datetime.now().timestamp() * 1000)
    data = PostDB.objects.get(id=pro_id)
    return render(req, "booking.html", {'data':data, 'current_time':current_time})

def cart(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('mobile')
        c = request.POST.get('email')
        d = request.POST.get('address')
        e = request.POST.get('city')
        f = request.POST.get('note')
        g = request.POST.get('amount')
        h = request.POST.get('ad_id')
        i = request.POST.get('booking_id')
        obj = OrderDB(Name=a, Mobile=b, Email=c, Address=d, City=e, Note=f, Amount=g, AdID=h, BookingID=i)
        obj.save()
        return redirect(client_home)
def cartview(request):
    data = OrderDB.objects.all()
    return render(request, "cartview.html", {'data':data})







# def cartSave(req):
#     if req.method=="POST":
#         pn = req.POST.get('pname')
#         q = req.POST.get('qty')
#         pr = req.POST.get('price')
#         t = req.POST.get('total')
#         un = req.POST.get('username')
#         try:
#             x = PostDB.objects.get(id=pn)
#             img = x.Image
#         except PostDB.DoesNotExist:
#             img = None
#         obj = BookingDB(ClientName=un, ProductName=pn, Quantity=q, Image=img, Price=pr, TotalPrice=t)
#         obj.save()
#         return redirect(client_home)

