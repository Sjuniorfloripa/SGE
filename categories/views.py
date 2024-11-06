from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from categories import models, forms, serializers


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model= models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10
    permission_required = 'categories.view_category'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
            
        return queryset

class CategoryCreateview(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required ='categories.add_category'
    
class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'
    context_object_name = 'categories'
    permission_required = 'categories.view_category'
    
class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    context_object_name = 'categories'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.change_category'
    

class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    context_object_name = 'categories'
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.delete_category' 

# APIs Views
class CategoryCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
