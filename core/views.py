from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bootstrap_modal_forms.generic import BSModalCreateView

from .models import Product
from .forms import ProductModelForm


class HomeView(ListView):
    """
        Display home page with a products list
    """
    model = Product
    template_name = 'core/index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


# class CreateProductView(CreateView):
#     """
#         Adds a product to the database
#     """
#     model = Product
#     template_name = 'core/product_add_form.html'
#     fields = ('name', 'price')
#     success_url = reverse_lazy('core:home')


class CreateProductView(BSModalCreateView):
    """
        Adds a product to the database
    """
    model = Product
    form_class = ProductModelForm
    template_name = 'core/add.html'
    success_message = 'Success: Product was adds'
    success_url = reverse_lazy("core:home")


class UpdateProductView(UpdateView):
    """
        Udpate a product
    """
    model = Product
    template_name = 'core/product_edit_form.html'
    fields = ('name', 'price')
    success_url = reverse_lazy('core:home')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'core/product_del_form.html'
    success_url = reverse_lazy('core:home')
