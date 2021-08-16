from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashboard_page"),
    path('products', views.products, name="product_page"),
    path('customer/<str:pk>', views.customer, name="customer"),
    # CRUD PATHS
    path('create_order', views.createOrder, name="create_order"),
    path('create_customer', views.createCustomer, name="create_customer"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('update_customer/<str:pk>', views.updateCustomer, name="update_customer"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('delete_customer/<str:pk>', views.deleteCustomer, name="delete_customer"),
    # AUTHENTICATION PATH
    path('login', views.loginPage, name="login"),
#     path('register', views.registerPage, name="register"),
    path('logout', views.logOut, name="logout"),



]
