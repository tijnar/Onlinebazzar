from django.urls import path

from shop.views import HomeView, ProductView, SignUpView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<str:product_slug>', ProductView.as_view(), name='product_page'),
    path('register', SignUpView.as_view(), name='register')
]
