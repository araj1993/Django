from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Order

def products_view(request):
    """
    Display all products
    """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/products.html', context)

@login_required
def order_history_view(request):
    """
    Display user's order history - protected route
    """
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    context = {
        'orders': orders,
    }
    return render(request, 'store/order_history.html', context)
