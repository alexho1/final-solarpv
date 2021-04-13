from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('api/', include('myapp.api.url', namespace='api')),
    path('search/', views.search, name='search'),
    path('search/<int:number>/', views.search_number, name='search_number'),
    path('search/<str:title>/', views.search_certificate, name='search_certificate'),
]