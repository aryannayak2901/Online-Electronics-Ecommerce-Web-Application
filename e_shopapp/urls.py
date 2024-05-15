from unicodedata import name
from django.contrib import admin
from django.urls import path
from e_shopapp import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
    path("signin", views.signin, name = 'signin'),
    path("signup", views.signup, name="signup"),
    path("signout", views.signout, name = "signout"),
    path("contact", views.contact, name = 'contact'),
    path("user_profile", views.user_profile, name='user_profile'),
    path("cart", views.cart_list, name='cart_list'),
    path("upload_product", views.upload_product, name='upload_product'),
    path("history", views.history, name='history'),
    path("product_view/<int:product_view_page_product_id>", views.product_view, name='product_view'),
    path("checkout", views.checkout, name= 'checkout'),
    path("tracker", views.tracker, name='tracker'),
    path("search", views.search, name='search'),
    path("handlerequest/", views.handlerequest, name='handlerequest'),
]
