from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('services/', views.service_details, name='service_details'),
    path('contact/', views.contact, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('portfolio/<int:id>/', views.portfolio_details, name='portfolio_details'),  # id é inteiro
    path('portfolio-details/', views.portfolio_details, name='portfolio_details')
]    