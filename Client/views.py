from django.shortcuts import render, redirect
from Client.models import ClientDB, BookingDB, OrderDB, ReviewDB, OrderPayDB, BookingPaymentDB
from User.models import PostDB
from Admin.models import CategoryDB
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import logout
from django.utils.text import slugify
import razorpay
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse





# Create your views here.
def client_index(request):
    cat = CategoryDB.objects.all()
    data = OrderDB.objects.filter(UserName=request.session['Email'])

    return render(request, "client_index.html", {'cat':cat, 'data':data})
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
    cat = CategoryDB.objects.all()

    processed_categories = [{"name": c.Name, "slug": slugify(c.Name)} for c in categories]
    return render(request, "client_home.html", {'ads':ads, 'categories':processed_categories, 'cat':cat})

# def filtered(request):
#     ads = PostDB.objects.all()
#     categories = CategoryDB.objects.all()
#     return render(request, "client_home.html", {'ads':ads, 'categories':categories})


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
    rating = ReviewDB.objects.filter(AdID=pro_id)
    ratings = ReviewDB.objects.filter(AdID=pro_id)
    rating_color=[]
    for rate in ratings:
        if rate.Rating in [4, 5]:
            color = "green"
        elif rate.Rating in [2, 3]:
            color = "yellow"
        else:
            color = "red"
        rating_color.append(
            {"color": color}
        )
    return render(request, "singleproduct.html", {'data':data, 'rating':rating, 'ratings':rating_color})


def ClientLogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(ClientLogin)

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
        un = request.POST.get('username')
        try:
            x = PostDB.objects.get(id=h)
            img = x.Image
        except PostDB.DoesNotExists:
            img = None
        obj = OrderDB(UserName=un, Name=a, Mobile=b, Email=c, Address=d, City=e, Note=f, Amount=g, AdID=h, BookingID=i)
        obj.save()
        return redirect(client_home)


def save_payment_details(request, booking_id):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        city = request.POST.get('city')
        amount = request.POST.get('amount')
        property_id = request.POST.get('property')
        booking_id = request.POST.get('booking_id')
        payment_status = request.POST.get('payment_status') == '1'  # Convert string to boolean

        # Optionally, you can use these variables to fetch or create the corresponding booking object
        # Assuming you have a model to store the booking details and payment status
        try:
            booking = BookingPaymentDB.objects.get(BookingID=booking_id)
            # Update the payment status if required
            booking.payment_status = payment_status
            booking.save()

            # You can add other details or modify as necessary
            # booking.name = name
            # booking.mobile = mobile
            # booking.email = email
            # booking.city = city
            # booking.amount = amount
            # booking.property_id = property_id
            # booking.save()

            return redirect('payment_success')  # Redirect to a success page or handle the response

        except BookingPaymentDB.DoesNotExist:
            return HttpResponse("Booking not found", status=404)

    return HttpResponse("Invalid request method", status=400)



# def SavePaymentHistory(request):
#     if request.method=="POST":
#         a = request.POST.get('name')
#         b = request.POST.get('mobile')
#         c = request.POST.get('email')
#         d = request.POST.get('address')
#         e = request.POST.get('city')
#         f = request.POST.get('note')
#         g = request.POST.get('amount')
#         h = request.POST.get('ad_id')
#         i = request.POST.get('booking_id')
#         un = request.POST.get('username')
#         try:
#             x = PostDB.objects.get(id=h)
#             img = x.Image
#         except PostDB.DoesNotExists:
#             img = None
#         obj = OrderPayDB(UserName=un, Name=a, Mobile=b, Email=c, Address=d, City=e, Note=f, Amount=g, AdID=h, BookingID=i)
#         obj.save()
#         return redirect(client_home)

def cartview(request):
    data = OrderDB.objects.filter(UserName=request.session['Email'])
    return render(request, "cartview.html", {'data':data})

def cartDelete(request, crt_id):
    a = OrderDB.objects.filter(id=crt_id)
    a.delete()
    return redirect(cartview)

# def payment(req):
#     data = OrderDB.objects.all()
#     customer = OrderDB.objects.order_by('-id').first()
#
#     payy = customer.Amount
#
#     amount = int(payy*100)
#     payy_str = str(amount)
#
#     if req.method=="POST":
#         order_currency = 'INR'
#         client = razorpay.Client(auth=('rzp_test_WR8gfHiUtMH080', 'ZFS9WcXnKA6i9jd1hoXO8xaJ'))
#         payment = client.order.create({'amount':amount, 'currency':order_currency})
#     return render(req,"payment.html", {'data':data,'customer':customer, 'payy_str':payy_str})


def payment(req, booking_id):
    customer = get_object_or_404(OrderDB, id=booking_id)

    amount = int(customer.Amount * 100)  # Convert to paisa for Razorpay
    order_currency = 'INR'

    try:
        client = razorpay.Client(auth=('rzp_test_WR8gfHiUtMH080', 'ZFS9WcXnKA6i9jd1hoXO8xaJ'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': 1})

        # Store payment ID in session (useful for verification later)
        req.session['razorpay_order_id'] = payment['id']

    except Exception as e:
        return render(req, "payment.html", {'customer': customer, 'error': f"Payment error: {str(e)}"})

    return render(req, "payment.html", {'customer': customer, 'payment': payment})


def paymenthistory(request):
    data = OrderDB.objects.filter(UserName=request.session['Email'])
    return render(request, "paymenthistory.html", {'data': data})




def payment_success(req, booking_id):
    customer = get_object_or_404(OrderDB, id=booking_id)

    # Update the payment status in the database
    customer.payment_status = True
    customer.save()

    return render(req, "success.html", {'customer': customer})


def careers(req):
    return render(req, "careers.html")

def review(req, pro_id):
    current_time = int(datetime.now().timestamp() * 1000)
    data = PostDB.objects.get(id=pro_id)
    return render(req, "review.html", {'data':data, 'current_time':current_time})

def save_review(request):
    if request.method=="POST":
        a = request.POST.get('name')
        b = int(request.POST.get('rating'))
        c = request.POST.get('title')
        d = request.POST.get('review')

        h = request.POST.get('ad_id')
        un = request.POST.get('username')
        if b in [4, 5]:
            color = "green"
        elif b in [2, 3]:
            color = "yellow"
        elif b == 1:
            color = "red"
        else:
            color = "black"

        try:
            x = PostDB.objects.get(id=h)
            img = x.Image
        except PostDB.DoesNotExists:
            img = None
        obj = ReviewDB(UserName=un, ClientName=a, Rating=b, Title=c, Review=d, AdID=h, Color=color)
        obj.save()
        return redirect(client_home)




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

