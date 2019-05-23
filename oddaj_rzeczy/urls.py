"""oddaj_rzeczy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import LandingPage, SignUpView, AdminListView, LoginView, SetAdminPermission, DeleteUserView, \
    ModifyUserView, CharityListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landing_page'),
    path('register/', include('django.contrib.auth.urls'), name='register'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('admin-list', AdminListView.as_view(), name='admin_list'),
    path('login', LoginView.as_view(), name='login2'),
    path('set-admin-permission', SetAdminPermission.as_view(), name='set_admin_permission'),
    re_path('delete-user/(?P<pk>(\d)+)', DeleteUserView.as_view(), name='delete_user'),
    re_path('modify-user/(?P<pk>(\d)+)', ModifyUserView.as_view(), name='modify_user'),
    path('charity-list', CharityListView.as_view(), name='charity_list'),
]
