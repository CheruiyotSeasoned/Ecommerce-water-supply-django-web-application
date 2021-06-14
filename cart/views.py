from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from water.models import Supplier
from .cart import Cart
from .forms import CartAddSupplierForm
@require_POST
def cart_add(request, supplier_id):
	cart = Cart(request)
	supplier = get_object_or_404(Supplier, id=supplier_id)
	form = CartAddSupplierForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(supplier=supplier,trip=cd['trip'],override_trip=cd['override'])
	return redirect('cart:cart_detail')
@require_POST
def cart_remove(request, supplier_id):
	cart = Cart(request)
	product = get_object_or_404(Supplier, id=supplier_id)
	cart.remove(supplier)
	return redirect('cart:cart_detail')
def cart_detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart': cart})