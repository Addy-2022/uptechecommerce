import secrets
from django.db import models
from users.models import Profile
from . paystack import Paystack

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='sliders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# category
class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


# product
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='product')
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# cart
class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart - {self.total}'
    
# cart product
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    subtotal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart - {self.cart.id}'

# order
ORDER_STATUS=(
    ('completed','completed'),
    ('pending','pending'),
    ('cancelled','cancelled'),    
) 

PAYMENT_METHOD=(
    ('paystack','paystack'),
    ('transfer','transfer'),
)

class Order(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)
    order_by = models.CharField(max_length=250)
    shipping_address = models.TextField()
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    discount = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS,null=True)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD, null=True, default='paystack')
    payment_complete = models.BooleanField(default=False, null=True)
    ref = models.CharField(max_length=255, null=True)


    def __str__(self):
        return f'{self.amount}::{str(self.id)}'

    #   ref generate
    def save (self,*args,**kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            obj_with_sm_ref = Order.objects.filter(ref=ref) 
            if not obj_with_sm_ref:
                self.ref = ref
        super().save(*args,**kwargs)

    def amount_value(self)-> int:
        return self.amount * 100

    # verify payment
    def verify_payment(self):
        paystack = Paystack()
        status,result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount']/ 100 ==self.amount:
                self.payment_complete = True
            self.save()
            if self.payment_complete:
                return True
            return False