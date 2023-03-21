from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Product,Category,Carts
from .serializers import (ProductSerializer,CategorySeializer,PostProductSerializer,ReviewSerializer,
Userserializer,UserProfileserializer,Cartsserializer,SimpleCartSerializer)
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import authentication, permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.



# user registration and login


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }   

class userRegistration(APIView):
   def post(self,request):
    serializer=Userserializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user=serializer.save()
        token=get_tokens_for_user(user)
        return Response({'msg':'successfull','token':token})
    return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)

    def get(self,request):
        serializer=UserProfileserializer(data=request.data)
        if serializer.is_valid():
            return Response()




class userProfileView(APIView):
    authenticate=[JWTAuthentication]
    permission_classes=[IsAuthenticated] 

    def get(self,request):
        serializer=UserProfileserializer(request.user)
        return Response(serializer.data)    

# To list all product,add product, update product and delete product 

class ProductViews(APIView):
    def get(self,request,):
        product=Product.objects.all()
        serializer=ProductSerializer(product,many=True) 
        return Response(serializer.data) 

    def post(self,request):
        serilizer=PostProductSerializer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data)  

# To get single product and its details   

class ProductDetail(APIView):
    def get(self,request,pk):
        product=get_object_or_404(Product,id=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def put(self,request,pk):
        product=get_object_or_404(Product,id=pk)
        serializer=PostProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        product=get_object_or_404(Product,id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

# To get all category and to add category

class CategoryList(APIView):
    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySeializer(category,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CategorySeializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# To get products according to category(flter)
class CategoryDetailAPIView(APIView):
    def get(self, request, name):
        products = Product.objects.filter(category__title=name)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
#  to add review and get review product wise
class ReviewViewApi(APIView):
   
    def get(self,request,pk):
        product=get_object_or_404(Product,id=pk)
        reviews=product.review.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(serializer.data)
   
    def post(self,request,pk):
        product=get_object_or_404(Product,id=pk) 
        serializer=ReviewSerializer(data=request.data,context={"product":product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Add to the cart and delete from the cart

class AddtoCart(APIView):
    authenticate=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request,pk):
        user=request.user
        product=get_object_or_404(Product,id=pk)
        serializer=Cartsserializer(data=request.data,context={'user':user,'product':product})
        serializer.is_valid(raise_exception=True)
        try:
            cart=Carts.objects.get(user=user,product=product)
            cart.qty+=1
            cart.save()
            return Response({"msg":"succes"})

        except:
            serializer.save(user=user,product=product)
            return Response(serializer.data,status=status.HTTP_409_CONFLICT)     


  
    def delete(self,request,pk)      :
        cart=get_object_or_404(Carts,id=pk)
        cart.delete()
        return Response({"msg:deleted"},status=status.HTTP_204_NO_CONTENT)    

# to view whole cart
class CartListView(APIView):
    def get (self,request):
        cart=Carts.objects.all()
        serializer=SimpleCartSerializer(cart, many=True)
        return Response(serializer.data)   


# To view the items which are added by user

class UserCartView(ModelViewSet):
    serializer_class = Cartsserializer
    queryset = Carts.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]

    def list(self, request, *args, **kwargs):
        qs=Carts.objects.filter(user=request.user)
        serializer=Cartsserializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self, request, *args, **kwargs):
        return Response(data={"msg":"no acces"})             

# check out or order the item which user want

class OrdersView(APIView):
    def post(self,request,pk):
        user=request.user
        product=get_object_or_404(Product,id=pk)
        serializer=Orderserializer(data=request.data,context={'user':user,'product':product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cart=user.carts_set.filter(product=product).first()
        cart.delete()
        return Response(serializer.data)        

         