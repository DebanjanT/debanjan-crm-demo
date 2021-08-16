from django.shortcuts import render, redirect
from .models import *
from .form import orderForm, customerForm, createUserForm
from .filter import orderFilter
# contrib.auth library for auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required





def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard_page')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_page')
            else:
                messages.info(request, '⚠ Wrong Credentials ! Please Check ')


    contex = {}
    return render(request, 'accounts/login.html', contex)

def logOut(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard_page') 
    else:
        form = createUserForm()
        if request.method == 'POST':
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ' 👋 Hi, your account was created. ')
                return redirect('login')
           
    context = {'register_form': form}
    return render(request, 'accounts/register.html', context)

# @staff_member_required(login_url='login')
@login_required(login_url='login')
def home(request):

    orders = Order.objects.all()
    total_orders = orders.count()
    customers = Customer.objects.all()

    # status_of_orders
    pending_order = orders.filter(dstatus='Pending').count()
    OFD_order = orders.filter(dstatus='Out for delivery').count()
    delivered_orders = orders.filter(dstatus='Delivered').count()

    hmcontext = {'orders': orders, 'customers': customers, 'total_orders': total_orders,
                 'pending': pending_order, 'OFD': OFD_order, 'Delivered': delivered_orders}

    return render(request, 'accounts/dashboard.html', hmcontext)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    pdcontext = {'products': products}

    return render(request, 'accounts/products.html', pdcontext)

@staff_member_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    orderfilter = orderFilter(request.GET, queryset=orders)
    orders = orderfilter.qs
    custcontex = {'orderFilter': orderFilter, 'customer': customer,
                  'orders': orders, 'total_orders': total_orders}
    return render(request, 'accounts/customer.html', custcontex)

@login_required(login_url='login')
def createCustomer(request):
    cid = Customer.objects.all()
    form = customerForm()
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'create_customer': form}
    return render(request, 'accounts/customer_form.html', context)

@login_required(login_url='login')
def createOrder(request):
    form = orderForm()
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'createorder_form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = orderForm(instance=order)
    if request.method == 'POST':
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'update_order_form': form}
    return render(request, 'accounts/update_order.html', context)

@login_required(login_url='login')
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = customerForm(instance=customer)
    if request.method == 'POST':
        form = customerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'update_customer_form': form, 'customer': customer}
    return render(request, 'accounts/update_customer.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'accounts/delete_order_confirmation.html', context)

@login_required(login_url='login')
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {'customer': customer, 'total_order': total_order}
    return render(request, 'accounts/delete_customer_confirmation.html', context)
