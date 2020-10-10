from django.urls import path
from home import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="home"),
    path('contact-us/', TemplateView.as_view(template_name='home/contact.html')),
    path('about-us/', TemplateView.as_view(template_name='home/about.html')),
    ]
