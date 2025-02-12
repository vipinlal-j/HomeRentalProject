
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Admin.models import CategoryDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from HouseRentalManagementSystem import settings
from User.models import userDB, PostDB
from Client.models import ClientDB, OrderDB
from User import views
import datetime


# Create your views here.

def index(req):

    categories = CategoryDB.objects.count()
    post = PostDB.objects.count()
    time = datetime.datetime.now()
    return render(req,"index.html", {'categories': categories, 'post':post, 'time':time})
def admin_home(request):
    return render(request,"admin_home.html")
def view_users(request):
    data = userDB.objects.all()
    return render(request, "viewusers.html", {'data':data})
def delete_user(req,cat_id):
    a= userDB.objects.filter(id=cat_id)
    a.delete()
    return redirect(view_users)

def AdminLogin(req):
    return render(req, "AdminLogin.html")
def AdminLoginAuth(request):
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('password')
        if User.objects.filter(username__contains=a).exists():
            x = authenticate(username=a, password=b)
            if x is not None:
                login(request,x)
                request.session['username'] = a
                request.session['password'] = b
                messages.success(request, "Welcome")
                return redirect(index)
            else:
                messages.warning(request, "invalid Password")
                return redirect(AdminLogin)
        else:
            messages.warning(request, "invalid Username")
            return redirect(AdminLogin)
def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(AdminLogin)

def AddCategory(request):
    return render(request, "add_category.html")
def SaveCategory(request):
    if request.method=="POST":
        a = request.POST.get('catname')
        b = request.POST.get('des')
        c = request.FILES['image']
        obj = CategoryDB(Name=a, Description=b, Image=c)
        obj.save()
        messages.success(request, "Saved Successfully")
        return redirect(AddCategory)
def display_categories(request):
    data = CategoryDB.objects.all()
    return render(request, "display_categories.html", {'data':data})

def editCat(req,cat_id):
    data = CategoryDB.objects.get(id=cat_id)
    return render(req,"editCat.html" ,{'data':data})

def updateCat(req,cat_id):
    if req.method == "POST":
        a = req.POST.get('catname')
        b = req.POST.get('des')
        c = req.FILES['image']
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=cat_id).Image
        CategoryDB.objects.filter(id=cat_id).update(Name=a, Description=b, Image=c)
        return redirect(display_categories)
def deleteCat(req,cat_id):
    a= CategoryDB.objects.filter(id=cat_id)
    a.delete()
    return redirect(display_categories())

def view_client(request):
    data = ClientDB.objects.all()
    return render(request, "view_client.html", {'data':data})
def delete_client(req,cat_id):
    a= ClientDB.objects.filter(id=cat_id)
    a.delete()
    return redirect(view_client)

def client_cart(request):
    data = OrderDB.objects.all()
    return render(request, "client_cart.html", {'data':data})