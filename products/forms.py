from django import forms
from products import models

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'description', 'serial_number', 'cost_price',
                  'selling_price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'category': 'Categoria',
            'brand': 'Marca',
            'description': 'Descrição',
            'serial_number': 'Número de Série',
            'cost_price': 'Valor de Custo',
            'selling_price': 'Valor de Venda',
        }