# from django import forms

from bootstrap_modal_forms.forms import BSModalModelForm

from .models import Product


# class ProductModelForm(forms.ModelForm):

#     class Meta:

#         model = Product
#         fields = ('name', 'price')


class ProductModelForm(BSModalModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price')
