from django.urls import path
from . import views

app_name = "account_url"

urlpatterns = [
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('signup/', views.SignUpFormView.as_view(), name='sign_up'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit/', views.UserEditView.as_view(), name='edit'),
    path('api/', views.UserApi.as_view(), name='api'),
]