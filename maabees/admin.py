from django.contrib import admin
from .models import  Feedback, Product, Userlogin,Userregister,Brand,Category,Whishlist,Cart,Oder,Address

# Register your models here.
admin.site.register(Userlogin)
admin.site.register(Userregister)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Whishlist)
admin.site.register(Cart)
admin.site.register(Oder)
admin.site.register(Address)
admin.site.register(Feedback)








