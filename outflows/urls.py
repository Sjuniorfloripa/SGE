from django.urls import path
from outflows import views


urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', views.OutflowCreateview.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),
    
    path('api/v1/outflows/', views.OutflowCreateListAPIView.as_view(), name='outflow-create-list-api-view'),
    path('api/v1/outflows/<int:pk>', views.OutflowRetrieveView.as_view(), name='outflow-detail-api-view')
]
