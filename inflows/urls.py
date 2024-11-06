from django.urls import path
from inflows import views


urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', views.InflowCreateview.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),
    
    path('api/v1/inflows/', views.InflowCreateListAPIView.as_view(), name='inflow-create-list-api-view'),
    path('api/v1/inflows/<int:pk>', views.InflowRetrieveView.as_view(), name='inflow-detail-api-view')
]
