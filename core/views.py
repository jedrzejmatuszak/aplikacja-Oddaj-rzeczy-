from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class LandingPage(View):

    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request):
        return render(request, 'registration/login.html')


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')
