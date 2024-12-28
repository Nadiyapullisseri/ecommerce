from datetime import datetime
from functools import partial
from re import L
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework .generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from . models import Address, Cart, Category, Feedback, Userregister,Userlogin,Brand,Product, Whishlist,Oder
from . serializers import AddressSerializer, CartSerializer, CategorySerializer, LoginSerializer, OderSerializer, ProductSerializer, RegisterSerializer,BrandSerializer, WhishlistSerializer,FeedbackSerializer
from django.db.models import Q
from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("homepage")

class user_register_view(GenericAPIView):
    serializer_class=RegisterSerializer
    def post(self,request):
        name=request.data.get('name')
        email=request.data.get('email')
        password=request.data.get('password')
        mobile_no=request.data.get('mobile_no')
        role='user'
        login_id=""
        
        if not name or not email or not password or not mobile_no:
            return Response({'message':'all fields are required'},status=status.HTTP_400_BAD_REQUEST)
        if Userregister.objects.filter(name=name).exists():
            return Response({'message':'name already exist'},status=status.HTTP_400_BAD_REQUEST)
        if Userregister.objects.filter(mobile_no=mobile_no).exists():
            return Response({'message':'mobile_no already exist'},status=status.HTTP_400_BAD_REQUEST)
        
        login_serializer=LoginSerializer(data={'email':email,
                                               'password':password,
                                               'role':role})
        if login_serializer.is_valid():
            l=login_serializer.save()
            login_id=l.id
        else:
            return Response({'message':'login failed'},status=status.HTTP_400_BAD_REQUEST)
        
        register_serializer=RegisterSerializer(data={'name':name,
                                                     'email':email,
                                                     'password':password,
                                                     'mobile_no':mobile_no,
                                                     'role':role,
                                                     'login_id':login_id})
        if register_serializer.is_valid():
            register_serializer.save()
            return Response({'message':'registration successfull'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'registarion failed'},status=status.HTTP_400_BAD_REQUEST)
            
            

class user_login_view(GenericAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        
        logins=Userlogin.objects.filter(email=email,password=password)
        print(logins)
        if(logins.count()>0):
            login_serializer=LoginSerializer(logins,many=True)
            
            for i in login_serializer.data:
                login_id=i['id']
                role=i['role']
                register_data=Userregister.objects.filter(login_id=login_id).values()
                for i in register_data:
                    name=i['name']
            return Response({'data':{'login_id':login_id,'name':name,'email':email,'password':password},'success':1,'message':'login successfull'})
        else:
            return Response({'message':'login faild'},status=status.HTTP_400_BAD_REQUEST)
        
        
class users_view(GenericAPIView):
    serializer_class=RegisterSerializer
    def get(self,request):
        users=Userregister.objects.all()
        if users.count()>0:
            user_serializer=RegisterSerializer(users,many=True)
            return Response({'data':user_serializer.data,'message':'get all data'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class one_user_view(GenericAPIView):
    serializer_class=RegisterSerializer
    def get(self,request,id):
        user=Userregister.objects.get(pk=id)
        one_user_serializer=RegisterSerializer(user)
        return Response(one_user_serializer.data)
    
    
class user_update_view(GenericAPIView):
    serializer_class=RegisterSerializer
    def put(self,request,id):
        user_update=Userregister.objects.get(pk=id)
        update_serializer=RegisterSerializer(instance=user_update,data=request.data,partial=True)
        if update_serializer.is_valid():
            update_serializer.save()
            return Response({'message':'user data updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'some error in updation'},status=status.HTTP_400_BAD_REQUEST)
        
        
class user_delete_view(GenericAPIView):
    serializer_class=RegisterSerializer
    def delete(self,request,id):
        user=Userregister.objects.get(pk=id)
        user.delete()
        return Response({'message':'deleted successfully'},status=status.HTTP_200_OK)
    
class brand_register_view(GenericAPIView):
    serializer_class=BrandSerializer
    def post(self,request):
        brand_name=request.data.get('brand_name')
        brand_email=request.data.get('brand_email')
        password=request.data.get('password')
        mobile_no=request.data.get('mobile_no')
        role='brand'
        login_id=""
        if not brand_name or not brand_email or not password or not mobile_no:
            return Response({'message':'all fields are requerd'},status=status.HTTP_400_BAD_REQUEST)
        if Brand.objects.filter(brand_name=brand_name).exists():
            return Response({'message':'shop_name already exist'},status=status.HTTP_400_BAD_REQUEST)
        if Brand.objects.filter(mobile_no=mobile_no).exists():
            return Response({'message':'mobile_no already exist'},status=status.HTTP_400_BAD_REQUEST)
        login_serializer=LoginSerializer(data={'email':brand_email,
                                               'password':password,
                                               'role':role})
        if login_serializer.is_valid():
            l=login_serializer.save()
            login_id=l.id
        else:
            return Response(login_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        brand_serializer=BrandSerializer(data={'brand_name':brand_name,
                                             'brand_email':brand_email,
                                             'password':password,
                                             'mobile_no':mobile_no,
                                             'role':role,
                                             'login_id':login_id})
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response({'message':'registartion successfull'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'registration faild'},status=status.HTTP_400_BAD_REQUEST)
        
        
class brand_login_view(GenericAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        brand_email=request.data.get('brand_email')
        password=request.data.get('password')
        brand_login=Userlogin.objects.filter(email=brand_email,password=password)
        if(brand_login.count()>0):
            brand_serializer=LoginSerializer(brand_login,many=True)
            for i in brand_serializer.data:
                login_id=i['id']
                role=i['role']
                register_data=Brand.objects.filter(login_id=login_id).values()
                print(register_data)
                for i in register_data:
                    brand_name=i['brand_name']
            return Response({'data':{'login_id':login_id,'email':brand_email,'brand_name':brand_name,'password':password},'success':1,'message':'login successfull'})
        else:
            return Response({'message':'login failed'},status=status.HTTP_400_BAD_REQUEST)
        
        
class brand_all_view(GenericAPIView):
    serializer_class=BrandSerializer
    def get(self,requst):
        brands=Brand.objects.all()
        if brands.count()>0:
            brand_serializer=BrandSerializer(brands,many=True)
            return Response({'data':brand_serializer.data,'message':'successfully get all data'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class brand_one_view(GenericAPIView):
    serializer_class=BrandSerializer
    def get(self,request,id):
        brand=Brand.objects.get(pk=id)
        brand_serializer=BrandSerializer(brand)
        return Response(brand_serializer.data)
            
    
class brand_update_view(GenericAPIView):
    serializer_class=BrandSerializer
    def put(self,request,id):
        brand_update=Brand.objects.get(pk=id)
        brand_serializer=BrandSerializer(instance=brand_update,data=request.data,partial=True)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response({'message':'updated data successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'data couldnot updata'},status=status.HTTP_400_BAD_REQUEST)
        
class brand_delete_view(GenericAPIView):
    serializer_class=BrandSerializer
    def delete(self,request,id):
        brands=Brand.objects.get(pk=id)
        brands.delete()
        return Response({'message':'deleted successfully'},status=status.HTTP_200_OK)
    
class category_add_view(GenericAPIView):
    serializer_class=CategorySerializer
    def post(self,request):
        category_name=request.data.get('category_name')
        category_image=request.data.get('category_image')
        if not category_name or not category_image:
            return Response({'message':'all fields are requerd'},status=status.HTTP_400_BAD_REQUEST)
        if Category.objects.filter(category_name=category_name).exists():
            return Response({'message':'duplicate names are not allowed'},status=status.HTTP_400_BAD_REQUEST)
        category_serializer=CategorySerializer(data={'category_name':category_name,'category_image':category_image})
        if category_serializer.is_valid():
            category_serializer.save()
            return Response({'message':'category successfully added'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'category doesnot added'},status=status.HTTP_400_BAD_REQUEST)
    
class category_view(GenericAPIView):
    serializer_class=CategorySerializer
    def get(self,request):
        categories=Category.objects.all()
        if categories.count()>0:
            category_serializer=CategorySerializer(categories,many=True)
            return Response({'data':category_serializer.data,'message':'successfully get all category'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class category_update_view(GenericAPIView):
    serializer_class=CategorySerializer
    def put(self,request,id):
        category=Category.objects.get(pk=id)
        category_serializer=CategorySerializer(instance=category,data=request.data,partial=True)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response({'message':'updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'couldnot update the data'},status=status.HTTP_400_BAD_REQUEST)
        
        
class category_delete_view(GenericAPIView):
    serializer_class=CategorySerializer
    def delete(self,request,id):
        category=Category.objects.get(pk=id)
        category.delete()
        return Response({'message':'deleted successfully'},status=status.HTTP_200_OK)
    
    
class product_add_view(GenericAPIView):
    serializer_class=ProductSerializer
    def post(self,request):
        product_name=request.data.get('product_name')
        product_price=request.data.get('product_price')
        product_image=request.data.get('product_image')
        category_id=request.data.get('category_id')
        brand_id=request.data.get('brand_id')
        if not product_name or not product_price or not product_image or not category_id  or not brand_id:
            return Response({'message':'all fields are required'},status=status.HTTP_400_BAD_REQUEST)
        if Product.objects.filter(product_name=product_name).exists():
            return Response({'message':'product_name already exist'},status=status.HTTP_400_BAD_REQUEST)
        try:
            category=Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'message':'invalid category id'},status=status.HTTP_400_BAD_REQUEST)
        try:
            brands=Brand.objects.get(id=brand_id)
        except Brand.objects.get(id=brand_id):
            return Response({'message':'invalid brand id'},status=status.HTTP_400_BAD_REQUEST)
        product_serializer=ProductSerializer(data={'product_name':product_name,
                                                   'product_price':product_price,
                                                   'product_image':product_image,
                                                   'category_id':category.id,
                                                   'brand_id':brands.id})  
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message':'product successfully added'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'product could not added'},status=status.HTTP_400_BAD_REQUEST)  
        
        
class product_view(GenericAPIView):
    serializer_class=ProductSerializer 
    def get(self,request):
        products=Product.objects.all()
        if products.count()>0:
            product_serializer=ProductSerializer(products,many=True)
            return Response({'data':product_serializer.data,'message':'successfully get all products'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        
        
class product_category_view(GenericAPIView):
    serializer_class=ProductSerializer
    def get(self,request,category_id):
        products=Product.objects.filter(category_id=category_id)
        if products.exists():
            product_serializer=ProductSerializer(products,many=True)
            return Response({'data':product_serializer.data ,'message':'successfully get all data'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class product_brand_view(GenericAPIView):
    serializer_class=ProductSerializer
    def get(self,request,brand_id):
        products=Product.objects.filter(brand_id=brand_id)
        if products.exists():
            product_serializer=ProductSerializer(products,many=True)
            return Response({'data':product_serializer.data,'message':'successfully get all data'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class product_update_view(GenericAPIView):
    serializer_class=ProductSerializer
    def put(self,request,id):
        products=Product.objects.get(pk=id)
        product_serializer=ProductSerializer(instance=products,data=request.data,partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message':'data updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class product_delete_view(GenericAPIView):
    serializer_class=ProductSerializer
    def delete(self,request,id):
        products=Product.objects.get(pk=id)
        products.delete()
        return Response({'message':'deleted successfully'},status=status.HTTP_200_OK)
            
class product_search_view(GenericAPIView):
    serializer_class=ProductSerializer
    def post(self,request):
        search_query=request.data.get('search_query','')
        if search_query:
            products=Product.objects.filter(Q(product_name__icontains=search_query)|Q(category_id__category_name__icontains=search_query)|Q(brand_id__brand_name__icontains=search_query))
            if not products.exists():
                return Response({'message':'product not found'},status=status.HTTP_400_BAD_REQUEST)
            product_serializer=self.serializer_class(products,many=True)
            return Response({'data':product_serializer.data,'message':'product fetched successfully'},status=status.HTTP_200_OK)
        return Response({'message':'no search query provided'},status=status.HTTP_400_BAD_REQUEST)
    
    
class whishlist_add_view(GenericAPIView):
    serializer_class=WhishlistSerializer
    def post(self,request):
        user_id=request.data.get('user_id')
        product_id=request.data.get('product_id')
        brand_id=request.data.get('brand_id')
        if not user_id or not product_id or not brand_id:
            return Response({'message':'all fields are requerd'},status=status.HTTP_400_BAD_REQUEST)
        whishlist=Whishlist.objects.filter(product_id=product_id,user_id=user_id).first()
        if whishlist:
            whishlist.delete()
            return Response({'message':'product remove from whishlist'},status=status.HTTP_200_OK)
        else:
            product_data=Product.objects.filter(id=product_id).first()
            if not product_data:
                return Response({'message':'product not found'},status=status.HTTP_400_BAD_REQUEST)
            product_name=product_data.product_name
            product_price=product_data.product_price
            product_image=product_data.product_image
            whishlist_serializer=WhishlistSerializer(data={'user_id':user_id,
                                                      'product_id':product_id,
                                                      'brand_id':brand_id,
                                                      'product_name':product_name,
                                                      'product_price':product_price,
                                                      'product_image':product_image})
            if whishlist_serializer.is_valid():
                whishlist_serializer.save()
                return Response({'message':'product succeessfully added to whishlist'},status=status.HTTP_200_OK)
            else:
                return Response(whishlist_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            
class whishlist_view(GenericAPIView):
    serializer_class=WhishlistSerializer
    def get(self,request,user_id):
        whishlist=Whishlist.objects.filter(user_id=user_id)
        if whishlist.exists():
            whishlist_serializer=WhishlistSerializer(whishlist,many=True)
            return Response({'data':whishlist_serializer.data,'message':'successfully get whislist'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'no item n whishlist'},status=status.HTTP_400_BAD_REQUEST)
        
class cart_add_view(GenericAPIView):
    serializer_class=CartSerializer
    def post(self,request):
        user_id=request.data.get('user_id')
        product_id=request.data.get('product_id')
        brand_id=request.data.get('brand_id')
        quantity=1
        cart_status=1
        if not user_id or not product_id or not brand_id:
            return Response({'message':'all fields are requared'},status=status.HTTP_400_BAD_REQUEST)
        cart=Cart.objects.filter(user_id=user_id,product_id=product_id)
        if cart.exists():
            return Response({'message':'item allredy in cart'},status=status.HTTP_400_BAD_REQUEST)
        else:
            cart_data=Product.objects.filter(id=product_id).first()
            print(cart_data)
            if not cart_data:
                return Response({'message':'product not found'},status=status.HTTP_400_BAD_REQUEST)
            product_name=cart_data.product_name
            product_price=cart_data.product_price
            product_image=cart_data.product_image
            cart_serializer=CartSerializer(data={'user_id':user_id,
                                                 'product_id':product_id,
                                                 'brand_id':brand_id,
                                                 'product_name':product_name,
                                                 'product_price':product_price,
                                                 'product_image':product_image,
                                                 'quantity':quantity,
                                                 'cart_status':cart_status})
            if cart_serializer.is_valid():
                cart_serializer.save()
                return Response({'message':'product successfully added to cart'},status=status.HTTP_200_OK)
            else:
                return Response(cart_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            
class cart_view(GenericAPIView):
    serializer_class=CartSerializer
    def get(self,request,user_id):
        carts=Cart.objects.filter(user_id=user_id)
        if carts.exists():
            cart_serializer=CartSerializer(carts,many=True)
            return Response({'data':cart_serializer.data,'message':'cart data successfully get'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'no item in cart'},status=status.HTTP_400_BAD_REQUEST)
        
class cart_delete_based_on_product(GenericAPIView):
    serializer_class=CartSerializer
    def delete(self,request,user_id,product_id):
        carts=Cart.objects.filter(user_id=user_id,product_id=product_id)
        carts.delete()
        return Response({'message':'successfully delete cart product'},status=status.HTTP_200_OK)
    
class cart_delete_view(GenericAPIView):
    serializer_class=CartSerializer
    def delete(self,request,user_id):
        carts=Cart.objects.filter(user_id=user_id)
        carts.delete()[0]
        return Response({'message':'successfully deleted carts'},status=status.HTTP_400_BAD_REQUEST)
    
    
class oder_product_view(GenericAPIView):
    serializer_class=OderSerializer
    def post(self,request,user_id):
        cart_item=Cart.objects.filter(user_id=user_id,cart_status=1)
        if cart_item.exists():
            oder=[]
            for i in cart_item:
                oder_data={'user_id':i.user_id,
                           'product_id':i.product_id,
                           'brand_id':i.brand_id,
                           'product_name':i.product_name,
                           'product_price':i.product_price,
                           'product_image':i.product_image,
                           'quantity':i.quantity}
                oder_serializer=OderSerializer(data=oder_data)
                if oder_serializer.is_valid():
                    oder_serializer.save()
                    oder.append(oder_serializer.data)
            cart_item.delete()
            return Response({'message':'oder the product successfully'},status=status.HTTP_200_OK)
        return Response({'message':'no item in cart'},status=status.HTTP_400_BAD_REQUEST)
    
    
class oder_view(GenericAPIView):
    serializer_class=OderSerializer
    def get(self,request,user_id):
        oders=Oder.objects.filter(user_id=user_id)
        if oders.exists():
            oder_serializer=OderSerializer(oders,many=True)
            return Response({'data':oder_serializer.data,'message':'oderd products'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'no oder placed'},status=status.HTTP_400_BAD_REQUEST)
        
        
class address_add_view(GenericAPIView):
    serializer_class=AddressSerializer
    def post(self,request,user_id):
        user_id=request.data.get('user_id')
        name=request.data.get('name')
        address=request.data.get('address')
        mobile_no=request.data.get('mobile_no')
        place=request.data.get('place')
        pin_code=request.data.get('pin_code')
        district=request.data.get('district')
        state=request.data.get('state')
        if not user_id or not name or not address or not mobile_no or not place or not pin_code or not district or not state:
            return response({'message':'all fields are requerd'},status=status.HTTP_400_BAD_REQUEST)
        if Address.objects.filter(name=name).exists():
            return Response({'message':'duplicate names are not allowed'},status=status.HTTP_400_BAD_REQUEST)
        address_serializer=AddressSerializer(data={'user_id':user_id,
                                                   'name':name,
                                                   'address':address,
                                                   'mobile_no':mobile_no,
                                                   'place':place,
                                                   'pin_code':pin_code,
                                                   'district':district,
                                                   'state':state})     
        if address_serializer.is_valid():
            address_serializer.save()
            return Response({'message':'address added successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'address does not added'},status=status.HTTP_400_BAD_REQUEST)    
        
        
class address_view(GenericAPIView):
    serializer_class=AddressSerializer
    def get(self,request,user_id):
        address=Address.objects.filter(user_id=user_id)
        if address.exists():
            address_serializer=AddressSerializer(address,many=True)
            return Response({'data':address_serializer.data,'message':'successully get the address'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)   
        
class address_update_view(GenericAPIView):
    serializer_class=AddressSerializer
    def put(self,request,user_id,id):
        address=Address.objects.get(user_id=user_id,pk=id)
        print(address)
        address_serializer=AddressSerializer(instance=address,data=request.data,partial=True)
        if address_serializer.is_valid():
            address_serializer.save()
            return Response({'message':'address updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response(address_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class address_delete_view(GenericAPIView):
    serializer_class=AddressSerializer
    def delete(self,request,user_id,id):
        address=Address.objects.get(user_id=user_id,pk=id)
        address.delete()
        return Response({'message':'deleted successfully'},status=status.HTTP_200_OK)
    
class feedback_add_view(GenericAPIView):
    serializer_class=FeedbackSerializer
    def post(self,request):
        user_id=request.data.get('user_id')
        product_id=request.data.get('product_id')
        description=request.data.get('description')
        if not user_id or not product_id or not description:
            return Response({'message':'all fields are requerd'},status=status.HTTP_400_BAD_REQUEST)
        date=timezone.now().isoformat()
        feedback_serializer=FeedbackSerializer(data={'user_id':user_id,
                                                     'product_id':product_id,
                                                     'description':description,
                                                     'date':date})
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return Response({'message':'feedback added successfully'},status=status.HTTP_200_OK)
        else:
            return Response(feedback_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class feedback_view(GenericAPIView):
    serializer_class=FeedbackSerializer
    def get(self,request,user_id):
        feedback=Feedback.objects.filter(user_id=user_id)
        if feedback.exists():
            feedback_serializer=FeedbackSerializer(feedback,many=True)
            return Response({'data':feedback_serializer.data,'message':'successfully get all feedbacks'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
class feedback_product_by_view(GenericAPIView):
    serializer_class=FeedbackSerializer
    def get(self,request,product_id):
        feedback=Feedback.objects.filter(product_id=product_id)
        if feedback.exists():
            feedback_serializer=FeedbackSerializer(feedback,many=True)
            return Response({'data':feedback_serializer.data,'message':' successfully get feedback of the products'},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class feedback_delete_view(GenericAPIView):
    serializer_class=FeedbackSerializer
    def delete(self,request,user_id,id):
        feedback=Feedback.objects.get(user_id=user_id,pk=id)
        feedback.delete()
        return Response({'message':'feedback deleted successfully'},status=status.HTTP_200_OK)
        
            
        
        
                
            
            
            
            