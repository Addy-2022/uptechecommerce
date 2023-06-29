from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('stores/', views.stores, name = 'stores'),
    path('store/<str:id>', views.store, name = 'store'),
    path('category/<str:id>', views.category, name = 'category'),
    path('search/', views.search, name = 'search'),
    path('addtocart/<str:id>',views.addtocart, name= 'addtocart'),
    path('mycart/',views.myCart, name= 'myCart'),
    path('managecart/<str:id>',views.manageCart, name= 'managecart'),
    path('checkout/<str:id>',views.checkout, name= 'checkout'),
    path('payment/<str:id>',views.payment, name= 'payment'),
    path('<str:ref>',views.verify_payment, name= 'verify-payment'),   
]