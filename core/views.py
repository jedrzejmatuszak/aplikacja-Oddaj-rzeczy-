from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class LandingPage(View):

    def get(self, request):
        return render(request, 'index.html')


class Test(View):

    def get(self, request):
        return HttpResponse('works')
