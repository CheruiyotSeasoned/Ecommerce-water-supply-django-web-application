from django import forms
SUPPLIER_TRIP_CHOICES = [{(i, str(i))} for i in range(1,21)]
class CartAddSupplierForm(forms.Form):
	trip =forms.TypedChoiceField(choices=SUPPLIER_TRIP_CHOICES,coerce=int)
	override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

















