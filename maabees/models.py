from ast import mod
from distutils.command.upload import upload
from django.utils  import timezone
from turtle import mode
from django.db import models

# Create your models here.

class Userlogin(models.Model):
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    role=models.CharField(max_length=40)


class Userregister(models.Model):
     name=models.CharField(max_length=40)
     email=models.CharField(max_length=40)
     password=models.CharField(max_length=40)
     mobile_no=models.IntegerField()
     role=models.CharField(max_length=40)
     login_id=models.OneToOneField(Userlogin,on_delete=models.CASCADE)
     
class Brand(models.Model):
    brand_name=models.CharField(max_length=40)
    brand_email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    mobile_no=models.IntegerField()
    role=models.CharField(max_length=40)
    login_id=models.OneToOneField(Userlogin,on_delete=models.CASCADE)
    
class Category(models.Model):
    category_name=models.CharField(max_length=40)
    category_image=models.ImageField(upload_to='category_image',null=True)
    
class Product(models.Model):
    product_name=models.CharField(max_length=40)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='product_image',null=True)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand_id=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
  
  
class Whishlist(models.Model):
    user_id=models.CharField(max_length=40)
    product_id=models.CharField(max_length=40)
    brand_id=models.CharField(max_length=40)
    product_name=models.CharField(max_length=40)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='whishlist_image',null=True)
    
class Cart(models.Model):
    user_id=models.CharField(max_length=40)
    product_id=models.CharField(max_length=40)
    brand_id=models.CharField(max_length=40)
    product_name=models.CharField(max_length=40)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='cart_image',null=True)
    quantity=models.IntegerField(default=1)
    cart_status=models.IntegerField(default=1)
    

class Oder(models.Model):
    user_id=models.CharField(max_length=40)
    product_id=models.CharField(max_length=40)
    brand_id=models.CharField(max_length=40)
    product_name=models.CharField(max_length=40)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='oder_image',null=True)
    quantity=models.IntegerField(default=1)
    oder_status=models.IntegerField(default=1)
    
class Address(models.Model):
    user_id=models.CharField(max_length=40)
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    mobile_no=models.IntegerField()
    pin_code=models.IntegerField()
    place=models.CharField(max_length=40)
    district=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    
    
class Feedback(models.Model):
    user_id=models.CharField(max_length=40)
    product_id=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    date=models.DateTimeField(default=timezone.now,auto_created=True)
    
    
