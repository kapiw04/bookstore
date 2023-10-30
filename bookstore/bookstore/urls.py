"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views as book_views
from cart import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_views.index, name='index'),
    path('details/<int:book_id>/', book_views.details, name='details'),
    path('add-to-cart/<int:book_id>/', book_views.addToCart, name='addToCart'),
    path('cart/', cart_views.cart, name='cart'),
    path('remove-from-cart/<int:book_id>/',
         cart_views.removeFromCart, name='removeFromCart'),
    path('checkout/', cart_views.checkout, name='checkout'),
    path('complete-order/<int:order_id>',
         cart_views.completeOrder, name='completeOrder')
]
