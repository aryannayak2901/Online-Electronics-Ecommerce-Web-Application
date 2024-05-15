from distutils.command.upload import upload
import email
from email.policy import default
from platform import mac_ver
from django.db import models

# Create your models here.

class User_details(models.Model):
    first_name = models.CharField(max_length=44, default="null", null=True)
    last_name = models.CharField(max_length=44, default="null", null=True)
    address = models.CharField(max_length=111, default="null", null=True)
    address2 = models.CharField(max_length=111, default="null", null=True)
    city = models.CharField(max_length=44, default="null", null=True)
    zip = models.CharField(max_length=44, default="null", null=True)
    phone_number = models.CharField(max_length=13, default="null", null=True)
    user_image = models.ImageField(upload_to = 'static/user_profile_images', default="shop/user_profile_default_image/user_profile_default_image.png")
    
    def __str__(self):
        return self.first_name

class Contact(models.Model):
    name = models.CharField(max_length=50, default="null", null=True)
    email = models.EmailField(max_length=122, default="null", null=True)
    phone = models.CharField(max_length=13, default="null", null=True)
    message = models.CharField(max_length=500, default="null", null=True)
    date = models.DateField()

    def __str__(self):
        return self.email

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length=400)
    publish_date = models.DateField(null=True)
    image = models.ImageField(upload_to = 'shop/images', default = "")
    seller_name = models.CharField(max_length=44, default="e_shop", null=True)

    def __str__(self):
        return self.product_name

class Orders(models.Model):
    product_list_for_checkout = models.CharField(max_length=500, default="")
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90, null=True, default="")
    email = models.CharField(max_length=111, null=True, default="")
    address = models.CharField(max_length=111, null=True, default="")
    city = models.CharField(max_length=30, null=True, default="")
    zip = models.CharField(max_length=11, null=True, default="")
    phone_number = models.CharField(max_length=13, null=True, default="")
    total_price = models.CharField(max_length=999999, default="null", null=False)

    def __str__(self):
        return str(self.order_id)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=400)
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7] + "..."