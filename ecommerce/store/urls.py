from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('product', views.product, name="product"),
    path('register', views.register, name="register"),
    path('login', views.loginn, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('cart', views.cart_page, name="cart_page"),
    path('add_Order/<product>', views.add_Order, name="add_Order"),
    path('remove_from_cart/<int:order_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('checkout/',views.checkout, name="checkout"),
    path('trackorder/',views.track_order, name="track_order"),
    path('update_order_status/', views.update_order_status, name="update_order_status"),
    path('review/',views.reviews, name="review"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
