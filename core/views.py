from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, ListView, DeleteView
from forms import LoginForm, SignUpForm, SetAdminPermissionForm


class LandingPage(View):

    def get(self, request):        return render(request, 'index.html')

    def post(self, request):
        return HttpResponse()


class LoginView(FormView):

    template_name = 'registration/login2.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(email=email)
        except Exception:
            msg = 'Nie ma takiego użytkownika'
            return render(self.request, 'registration/login2.html', {'form': form, 'msg': msg})
        authenticate(username=user.username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('/')
            else:
                msg = 'Użytkownik jest nieaktywny. Skontaktuj się z administratorem'
                return render(self.request, 'registration/login2.html', {'form': form, 'msg': msg})

    def form_invalid(self, form):
        msg = "Niepoprawne dane"
        return render(self.request, 'registration/login2.html', {'form': form, 'msg': msg})


class SignUpView(FormView):

    form_class = SignUpForm
    success_url = reverse_lazy('landing_page')
    template_name = 'register.html'

    def form_valid(self, form):
        if form.cleaned_data['password1'] == form.cleaned_data['password2']:
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'],
                )
                user_group = Group.objects.get(name='Użytkownik')
                user_group.user_set.add(user)
                return redirect('landing_page')
            except Exception:
                msg = 'Taki użytkownik już istnieje'
                return render(self.request, 'register.html', {'form': form, 'msg': msg})
        else:
            msg = 'Hasła są niezgodne'
            return render(self.request, 'register.html', {'form': form, 'msg': msg})


class AdminListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'User.add_permission'
    login_url = '/'

    def get(self, request):
        admins = User.objects.filter(groups__name='Administrator')
        return render(request, 'adminList.html', {'admins': admins})


class SetAdminPermission(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'User.add_permission'
    login_url = '/'
    form_class = SetAdminPermissionForm
    template_name = 'SetAdminPermission.html'

    def form_valid(self, form):
        username = form.cleaned_data['user']
        user = User.objects.get(username=username[0])
        group_admin = Group.objects.get(name='Administrator')
        group_admin.user_set.add(user)  # Dodaje obiekt User do grupy administrator
        if user.groups.filter(name='Użytkownik').exists():
            Group.objects.get(name='Użytkownik').user_set.remove(user)  # Usuwa obiekt User z grupy użytkownik
        return redirect('admin_list')


class DeleteUserView(DeleteView):
    model = User
    success_url = '/admin-list'
