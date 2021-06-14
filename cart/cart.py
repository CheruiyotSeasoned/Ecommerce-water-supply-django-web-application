from decimal import Decimal
from django.conf import settings
from water.models import Supplier
class Cart(object):
	def __init__(self, request):
		"""
		Initialize the cart.
		"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# save an empty cart in the session
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart
	def add(self,supplier,trip=1, override_trip=False):
	
		supplier_id = str(supplier.id)
		if supplier_id not in self.cart:
			self.cart[supplier_id] = {'trip': 0,
			'price': str(supplier.price)}
		if override_trip:
			self.cart[supplier_id]['trip'] = trip
		else:
			self.cart[supplier_id]['trip'] += trip
		self.save()
	def save(self):
		# mark the session as "modified" to make sure it gets saved
		self.session.modified = True
	def remove(self, supplier):
		supplier_id = str(supplier.id)
		if supplier_id in self.cart:
			del self.cart[supplier_id]
			self.save()
	def __iter__(self):

		supplier_ids = self.cart.keys()
		# get the supplier objects and add them to the cart
		suppliers = Supplier.objects.filter(id__in=supplier_ids)
		cart = self.cart.copy()
		for suplier in suppliers:
			cart[str(supplier.id)]['supplier'] = supplier
		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['trip']
			yield item
	def __len__(self):
		
		return sum(item['trip'] for item in self.cart.values())
	def __len__(self):

		return sum(item['trip'] for item in self.cart.values())
	def clear(self):
		# remove cart from session
		del self.session[settings.CART_SESSION_ID]
		self.save()
