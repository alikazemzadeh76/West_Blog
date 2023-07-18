from django.urls import path
from . import views

app_name = "home_url"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sidebar', views.sidebar, name='sidebar_url'),

]