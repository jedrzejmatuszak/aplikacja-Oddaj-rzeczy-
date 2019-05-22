from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


class LandingPage(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):

        return HttpResponse()


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('landing_page')
    template_name = 'register.html'


class TestView(View):

    def get(self, request):
        return render(request, 'base.html')
