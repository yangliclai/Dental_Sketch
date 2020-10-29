from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('patients/faq', views.faq, name='faq'),
    # path('contact.html', views.contact, name='contact'),
]
