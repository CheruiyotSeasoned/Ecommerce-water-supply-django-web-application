from django.shortcuts import render, get_object_or_404
from .models import Category, Supplier
from cart.forms import CartAddSupplierForm

def supplier_list(request, category_slug=None):

	category = None
	categories = Category.objects.all()
	suppliers = Supplier.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		suppliers = suppliers.filter(category=category)
	return render(request,
					'water/supplier/list.html',
					{'category':category,
					'categories':categories,
					'suppliers':suppliers})	

def supplier_detail(request, id, slug):	
	supplier = get_object_or_404(Supplier,id=id,slug=slug,available=True)
	cart_supplier_form = CartAddSupplierForm()
	return render(request,'water/supplier/detail.html',{'supplier':supplier,'cart_supplier_form': cart_supplier_form})	












