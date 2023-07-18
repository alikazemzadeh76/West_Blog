from django.urls import path
from . import views

app_name = 'contact_us'


urlpatterns = [
    path('contact/', views.ContactUsView.as_view(), name='contact'),
]