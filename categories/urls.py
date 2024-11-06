from django.urls import path
from categories import views


urlpatterns = [
    path('categories/list/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateview.as_view(), name='category_create'),
    path('categories/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    path('api/v1/categories/', views.CategoryCreateListAPIView.as_view(), name='category-create-list-api-view'),
    path('api/v1/categories/<int:pk>', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail-api-view')
]
