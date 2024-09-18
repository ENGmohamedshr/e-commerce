from django.urls import include, path


urlpatterns =[
   path('shop/',include('shop.urls')), 
   path('user/',include('user.urls')), 
   path('cart/',include('cart.urls')), 
]