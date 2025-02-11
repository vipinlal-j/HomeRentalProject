from django.shortcuts import render, redirect
from Client.models import ClientDB
from User.models import PostDB
from Admin.models import CategoryDB
from django.contrib import messages


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
