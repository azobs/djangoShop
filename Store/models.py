from django.db import models # type: ignore

# Create your models here.
#Model Category
class Category(models.Model):
    name = models.CharField(max_length=255)
#Model product
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


#Model customer
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    

#Model Address
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    
#Model Order
class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'
    
    PAYMENT_STATUS = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    status_payment = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS,
        default=PENDING
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

#Model OrderItems
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    
#Model Cart
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
#Model CartItems
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()