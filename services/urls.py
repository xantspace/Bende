from django.urls import path
from . import views

urlpatterns = [
    path('birth_cert/', views.birth_cert_view, name='birth_cert'),
    path('marriage_reg/', views.marriage_reg, name='marriage_reg'),
    path('waste_mgt/', views.waste_mgt, name='waste_mgt'),
    path('permit/', views.permit, name='permit'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
