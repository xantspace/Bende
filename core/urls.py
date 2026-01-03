from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
