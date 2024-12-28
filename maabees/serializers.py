

from dataclasses import fields
from rest_framework import serializers
from .models import  Address, Cart, Feedback, Oder, Product, Userlogin,Userregister,Brand,Category, Whishlist


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userlogin
        fields='__all__'
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userregister
        fields='__all__'
        
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class WhishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Whishlist
        fields='__all__'
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
        
class OderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Oder
        fields='__all__'
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'