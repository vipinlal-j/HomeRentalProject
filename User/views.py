from django.shortcuts import render, redirect
from User.models import userDB, PostDB
from django.contrib.auth import authenticate, login
from Admin.models import CategoryDB
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from HouseRentalManagementSystem import settings

# Create your views here.
def index(request):
    return render(request, "index.html")
def user_register(request):
    return render(request, "user_login.html")
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
        return redirect(user_register)
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

        obj = PostDB(Category=a, Rooms=b, Kitchen=c, Information=d, City=e, Rent=f,Mobile=g, Image=h)
        obj.save()
        return redirect(add_post)