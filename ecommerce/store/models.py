from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(("Quantity"))
    created_at = models.DateTimeField(default=timezone.now)
    ORDER_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        # Add more status options as needed
    )
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Pending')
    
    
    PAYMENT_METHOD_CHOICES = (
        ('Pending', 'Pending'),
        ('cod', 'Cash on Delivery'),
        ('credit_card', 'Credit Card'),
        # Add more payment methods as needed
    )
   
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='Pending')
    
    
   

    def __str__(self):
        return f'{self.user} --- {self.product}'
    
    
class Order_Successful(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(("Quantity"))
    created_at = models.DateTimeField(default=timezone.now)
    ORDER_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        # Add more status options as needed
    )
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Pending')
    
    
    PAYMENT_METHOD_CHOICES = (
        ('Pending', 'Pending'),
        ('cod', 'Cash on Delivery'),
        ('credit_card', 'Credit Card'),
        # Add more payment methods as needed
    )
   
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='Pending')
    
    
   

    def __str__(self):
        return f'{self.user} --- {self.product}'
    
    
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, default=1)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.user.username}'s Shipping Address"
    
    
    @property
    def product_name(self):
        return self.product.name if self.product else ''