from django.contrib import admin

from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/', views.add),
    path('Signup/',views.signup),
    path('card',views.card),
    path('cart/',views.cart),
    path('',views.gg),
    path('adminproducts/',views.products),
    path('cardproducts/',views.productcard),
    path('ff/',views.emp),
    path('mobiles/',views.mproducts),
    path('newmobiles/',views.showmobiles),
    path('oneplus/',views.one),
    path('redmi/',views.red),
    path('logout/',views.logout_view),
    path('home',views.bas)

]
