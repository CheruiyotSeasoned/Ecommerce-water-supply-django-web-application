from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('water:supplier_list_by_category',args=[self.slug])

class Supplier(models.Model):
	category = models.ForeignKey(Category, related_name='suppliers',on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='suppliers/%Y/%m/%d',blank=True)
	description = models.TextField(blank=True)
	capacity = models.CharField(max_length = 80, db_index=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	available = models.BooleanField(default=True)


	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
	def __str__(self):	
		return self.name

	def get_absolute_url(self):	
		return reverse('water:supplier_detail',args=[self.id, self.slug])