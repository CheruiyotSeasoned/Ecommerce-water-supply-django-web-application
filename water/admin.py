from django.contrib import admin
from .models import Category, Supplier


@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
	list_display=['name','slug']
	prepopulated_fields={'slug':('name',)}

@admin.register(Supplier)

class SupplierAdmin(admin.ModelAdmin):
	list_display = ['name','slug','price','capacity','available']
	list_filter = ['available','capacity','price']
	list_editable = ['price','available']
	prepopulated_fields = {'slug':('name',)}



