# myg-backend
 These all are the api endpoints
 
 This project is developed with djangorestframework


  
	
	
	
	 #to register and get the token
    ->signup
   
   
    # to access token for login
    ->token/
    
    
    # to view the token profile
    ->profile
    
    
    # To get all products
    ->all/products
    
    
    # to get detail of product , add product and delete product
    ->product/<int:pk>
    
    
    # to get list of category and add category
    ->category
    
    
    # category detail view and products based on category
    ->category/<str:name>
    
    
    # add review and get review
    ->product/review/<int:pk>
    
    
    # to add products to cart
    ->add/cart/<int:pk>
    
    
    # to view whole cart
    ->viewcart
    
    
    #To order the items
    ->orders/<str:pk>
    
    
    #to view cart items
    ->cart/items
