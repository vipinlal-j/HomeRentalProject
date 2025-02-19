from django.db import models
import uuid

# Create your models here.
class ClientDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
class BookingDB(models.Model):
    ClientName = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    AdID = models.IntegerField(null=True, blank=True)
    Amount = models.IntegerField(null=True, blank=True)
    UserName = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)

class OrderDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Note = models.CharField(max_length=50, null=True, blank=True)
    Amount = models.IntegerField(null=True, blank=True)
    AdID = models.IntegerField(null=True, blank=True)
    BookingID = models.IntegerField(null=True, blank=True)
    UserName = models.CharField(max_length=25, null=True, blank=True)
    payment_status = models.BooleanField(default=False)  # Store payment status

    def __str__(self):
        return f"{self.Name} - {self.BookingID}"


class OrderPayDB(models.Model):
    Name = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=20)
    Email = models.EmailField()
    City = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    AdID = models.CharField(max_length=50)
    BookingID = models.CharField(max_length=50)
    payment_status = models.BooleanField(default=False)  # Store payment status

    def __str__(self):
        return f"{self.Name} - {self.BookingID}"


class ReviewDB(models.Model):
    Rating = models.IntegerField(null=True, blank=True)
    Title = models.CharField(max_length=100, null=True, blank=True)
    Review = models.CharField(max_length=1000, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)
    AdID = models.CharField(max_length=50)
    ClientName = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    UserName = models.CharField(max_length=25, null=True, blank=True)
    Color = models.CharField(max_length=10, null=True, blank=True)


class BookingPaymentDB(models.Model):
    # Basic user details
    name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    # Property details
    property_id = models.CharField(max_length=50)  # Unique ID for the property
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Booking details
    booking_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)

    # Payment status
    payment_status = models.BooleanField(default=False)  # False means "Not Paid", True means "Paid"

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.booking_id} - {self.name}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
