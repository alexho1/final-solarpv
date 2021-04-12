from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('company/', views.CompanyListView.as_view(), name='company_list'),
    path('company/<pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
]