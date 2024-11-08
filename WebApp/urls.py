from django.urls import path
from WebApp import views
urlpatterns=[
path('homepage/',views.homepage,name="homepage"),
path('aboutpage/',views.aboutpage,name="aboutpage"),
path('Contactpage/',views.Contactpage,name="Contactpage"),
path('save_contact/',views.save_contact,name="save_contact"),
path('Classpage/',views.Classpage,name="Classpage"),
path('save_class/',views.save_class,name="save_class"),
path('product_list', views.product_list, name='product_list'),
path('category/<int:id>/', views.category_detail, name='category_detail'),
path('Teampage/',views.Teampage,name="Teampage"),
path('save_team/',views.save_team,name="save_team"),
path('testimonials/', views.testimonials, name='testimonials'),
path('save_testimonial/',views.save_testimonial,name="save_testimonial"),
path('all_products/',views.all_products,name="all_products"),
path('single_product/<int:pro_id>',views.single_product,name="single_product"),
path('filtered_products/<cat_name>',views.filtered_products,name="filtered_products"),
path('filtered_products/', views.filtered_products, name='filtered_products_empty'),
path('products/<str:cat_name>/', views.filtered_products, name='filtered_products'),
path('save_cart/',views.save_cart,name="save_cart"),
path('save_cart_wishlist/',views.save_cart_wishlist,name="save_cart_wishlist"),
path('cart_page/',views.cart_page,name="cart_page"),
path('checkout_page/',views.checkout_page,name="checkout_page"),
path('delete_cart/<int:data_id>/',views.delete_cart,name="delete_cart"),
path('registration/',views.registration,name="registration"),
path('save_registration/',views.save_registration,name="save_registration"),
path('',views.loginpage,name="loginpage"),
path('Userlogin/',views.Userlogin,name="Userlogin"),
path('User_logout/',views.User_logout,name="User_logout"),
path('apply_discount/', views.apply_discount, name='apply_discount'),
path('orderpage/',views.orderpage,name="orderpage"),
path('save_order/',views.save_order,name="save_order"),
path('wishlist/', views.wishlist, name='wishlist'),
path('save_wishlist', views.save_wishlist, name='save_wishlist'),
path('wishlist/delete/<int:item_id>/', views.delete_item, name='delete_item'),
path('class_list_view/', views.class_list_view, name='class_list_view'),
path('payment_success/',views.payment_success,name="payment_success"),
path('chatpage/',views.chatpage,name="chatpage"),



]