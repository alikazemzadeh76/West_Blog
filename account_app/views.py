from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import SignUpForm, EditUserForm, LoginForm
from django.views.generic import FormView, UpdateView
from django.urls import reverse_lazy
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



def log_out(request):
    logout(request)
    return redirect('home_url:home')

def user_profile(request):
        return render(request, "account_app/profile.html", {})


class LoginFormView(FormView):
    template_name = 'account_app/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_url:home')

    def form_valid(self, form):
        data = form.cleaned_data.get('username')
        user = User.objects.get(username=data)
        auth_login(self.request, user)

        return super().form_valid(form)
    
    
class SignUpFormView(FormView):
    template_name = 'account_app/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('account_url:profile')
    
    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create(**data)
        
        return super().form_valid(form)


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'account_app/user_edit.html'
    success_url = reverse_lazy('account_url:edit')

    def get_object(self, queryset=None):
        return self.request.user


class UserApi(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serialiser = UserSerializer(instance=queryset, many=True)
        return Response(data=serialiser.data)























