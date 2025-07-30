from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from main.models import Product
from main.forms import ProductForm
from main.filters import ProductFilters
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductImageFormSet

# Create your views here.

def index(request):
    product = Product.objects.all()
    product_filter = ProductFilters(request.GET, queryset=product)
    return render(request, 'index.html', locals())

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', locals())


def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        formset = ProductImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product
            formset.save()
            return redirect('index')  # Или куда нужно после создания
    else:
        form = ProductForm()
        formset = ProductImageFormSet()

    return render(request, 'create.html', {'form': form, 'formset': formset})

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            continue  # если товар удалён — пропускаем
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart

    return redirect('cart')

def remove_from_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id_str = str(product_id)
        if product_id_str in cart:
            del cart[product_id_str]
            request.session['cart'] = cart
    return redirect('cart')
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        formset = ProductImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product
            formset.save()
            return redirect('index')  # или куда нужно
    else:
        form = ProductForm()
        formset = ProductImageFormSet()

    return render(request, 'create.html', {'form': form, 'formset': formset})