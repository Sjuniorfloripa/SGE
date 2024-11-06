from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products import models, forms, serializers
from products.models import Product
from brands.models import Brand
from app import metrics


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serial_number = self.request.GET.get('serial_number')
        Product = self.request.GET.get('Product')
        brand = self.request.GET.get('brand')
        
        
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        if serial_number:
            queryset = queryset.filter(serial_number__icontains=serial_number)
        
        if Product:
            queryset = queryset.filter(Product__id=Product)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Product.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics'] = metrics.get_product_metrics()
        return context

class ProductCreateview(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'
    
class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'
    
class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    context_object_name = 'products'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    context_object_name = 'products'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product' 

# APIs Views
class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
