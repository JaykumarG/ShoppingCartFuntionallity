from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name = 'home'),
    path("cart/", views.cart, name = 'cart'),
    path("addtocart", views.Addtocart.as_view()),
]