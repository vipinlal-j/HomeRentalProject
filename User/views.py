from django.shortcuts import render, redirect
from User.models import userDB, PostDB
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from Admin.models import CategoryDB
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from HouseRentalManagementSystem import settings
from Client.models import OrderDB

# Create your views here.
def UserIndex(request):
    return render(request, "userindex.html")
def RegisterUser(request):
    return render(request, "UserRegister.html")
def user_save(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('mobile')
        d = request.POST.get('password')
        e = request.POST.get('city')
        f = request.POST.get('address')

        obj = userDB(Name=a, Email=b, Mobile=c, Password=d, City=e, Address=f)
        obj.save()
        return redirect(RegisterUser)



def UserLogin(request):
    return render(request, "UserLogin.html")
def UserLoginAuth(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        psw = request.POST.get('pass')
        if userDB.objects.filter(Email=un, Password=psw).exists():
            request.session['Email'] = un
            request.session['Password'] = psw
            messages.success(request, "Welcome")
            return redirect(UserIndex)
        else:
            messages.warning(request, "invalid Password")
            return redirect(UserLogin)
    else:
        messages.warning(request, "invalid Username")

def UserLogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(UserLogin)

def add_post(request):
    Name = CategoryDB.objects.all()
    return render(request, "add_post.html", {"Name":Name})

def save_post(request):
    if request.method=="POST":
        a = request.POST.get('cat')
        b = request.POST.get('rooms')
        c = request.POST.get('kitchen')
        d = request.POST.get('information')
        e = request.POST.get('city')
        f = request.POST.get('rent')
        g = request.POST.get('mobile')
        h = request.FILES['image']
        i = request.POST.get('email')


        obj = PostDB(Category=a, Rooms=b, Kitchen=c, Information=d, City=e, Rent=f,Mobile=g, Image=h, Email=i)
        obj.save()
        return redirect(add_post)

def ViewBookings(request):
    data = PostDB.objects.filter(Email=request.session['Email'])
    return render(request, "ViewBookings.html", {'data':data})

def PostDelete(request, crt_id):
    a= PostDB.objects.filter(id=crt_id)
    a.delete()
    return redirect(ViewBookings)


