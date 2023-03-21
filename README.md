# myg-backend
These all are the api endpoints

    # to register and get the token
    path("signup",views.userRegistration.as_view()),
    # to access token for login
    path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # to view the token profile
    path("profile",views.userProfileView.as_view()),
    # To get all products
    path("all/products",views.ProductViews.as_view()),
    # to get detail of product , add product and delete product
    path("product/<int:pk>",views.ProductDetail.as_view()),
    # to get list of category and add category
    path("category",views.CategoryList.as_view()),
    # category detail view and products based on category
    path("category/<str:name>",views.CategoryDetailAPIView.as_view()),
    # add review and get review
    path("product/review/<int:pk>",views.ReviewViewApi.as_view()), 
    # to add products to cart
    path("add/cart/<int:pk>",views.AddtoCart.as_view()),
    # to view whole cart
    path("viewcart",views.CartListView.as_view()),
    #To order the items
    path("orders/<str:pk>",views.OrdersView.as_view()),
    # path("orderall",views.OrderAllView.as_view()),
