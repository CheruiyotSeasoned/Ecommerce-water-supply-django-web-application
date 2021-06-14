from django.urls import path 
from . import views

app_name = 'water'

urlpatterns = [

	path('',views.supplier_list, name='supplier_list'),
	path('<slug:category_slug>/', views.supplier_list,name='supplier_list_by_category'),
	path('<int:id>/<slug:slug>/', views.supplier_detail,name='supplier_detail'),



]









