#urls.py 
from django.urls import path,include
from .views import *


urlpatterns = [
    # path('' ,Home, name='home-page'),
    # path('about/',About, name='about-page'),
    # path('contact/',Contact, name='contact-page'),
    # path('addproduct/',AddProduct, name='addproduct-page'),
    # path('allproduct/',Product, name='allproduct-page'),
    # path('register/',Register, name='register-page'),


    # path('product/api/',api_allproduct,name='product_api'),
    # path('detail/api/<int:pid>',api_product_detail),
    # path('create/product/',api_post_product),
    # path('put/product/<int:pid>',api_update_product),
    # path('delete/product/<int:pid>',api_delete_product),
    path('symbol',api_get_symbol),
    path('stock/<str:symbol>',api_get_stock)
]
