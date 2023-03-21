from rest_framework import serializers
from .models import Product,Category,Review,Carts,Orders
from django.contrib.auth.models import User



class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  "username",
                  "email",
                  "password"
                  ]

        extra_kwargs={
                       'email':{"required":True}
                  }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                 'id',
                  "username",
                  "email",
                  ]
                           


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=[
            "id","title"
        ]    

class ProductSerializer(serializers.ModelSerializer):
    category=CategorySeializer()
    class Meta:
        model=Product
        fields=[
            'id','name','description','category','image','price'
        ]


class PostProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'id','name','description','category','image','price'
        ]
             
class ReviewSerializer(serializers.ModelSerializer):
  
    product = serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields='__all__'
     
    
    def create(self, validated_data):
        product=self.context.get("product")
        return Review.objects.create(product=product,**validated_data)


class Cartsserializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
  

    class Meta:
        model=Carts
        fields = [
            
            "user",
            "product_id",
            "product",
            "date",
            "qty",
            "status"
        ]      

class SimpleCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carts
        fields = [
            "id",
            "user",
            "product",
            "date",
            "qty",
            "status"
        ]      
          

# class Orderserializer(serializers.ModelSerializer):
#     user = serializers.CharField(read_only=True)
#     product = serializers.CharField(read_only=True)
#     class Meta:
#         model=Orders
#         exclude = ['id']
#     def create(self, validated_data):
#         user=self.context.get("user")
#         product=self.context.get("product")
#         return Orders.objects.create(user=user,product=product,**validated_data)    