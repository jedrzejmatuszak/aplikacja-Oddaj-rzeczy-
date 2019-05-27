from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, DeleteView, UpdateView, CreateView
from .models import Charity
from .forms import LoginForm, SignUpForm, SetAdminPermissionForm, AddAdminForm, AddCharityForm, ModifyProfileForm, \
    ChangePasswordForm


class LandingPage(View):

    def get(self, request):
        return render(request, 'index.html')

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
            u = User.objects.get(email=email)
        except Exception:
            msg = 'Nie ma takiego użytkownika'
            return render(self.request, 'registration/login2.html', {'form': form, 'msg': msg})
        user = authenticate(username=u.username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('/')
            else:
                msg = 'Użytkownik jest nieaktywny. Skontaktuj się z administratorem'
                return render(self.request, 'registration/login2.html', {'form': form, 'msg': msg})
        else:
            msg = "Błędne hasło lub email"
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
    login_url = '/login'

    def get(self, request):
        admins = User.objects.filter(groups__name='Administrator')
        return render(request, 'adminList.html', {'admins': admins})


class SetAdminPermission(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'User.add_permission'
    login_url = '/login'
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


class AddAdminView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    login_url = 'login'
    permission_required = 'User.add_user'
    form_class = AddAdminForm
    #TODO: Does this view is really need?



class DeleteUserView(DeleteView):
    model = User
    success_url = '/admin-list'


class ModifyUserView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name_suffix = '_update_form'
    success_url = '/admin-list'
    #todo: zalinkować przycisk dodaj administratora


class CharityListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Charity
    fields = '__all__'
    ordering = ['id']


class CharityAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'login'
    permission_required = 'Charity.add_charity'
    model = Charity
    form_class = AddCharityForm
    success_url = 'charity-list'


class CharityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'login'
    permission_required = 'Charity.change_charity'
    model = Charity
    form_class = AddCharityForm
    template_name_suffix = '_update_form'
    success_url = '/charity-list'


class CharityDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'login'
    permission_required = 'Charity.delete_charity'
    model = Charity
    success_url = reverse_lazy('charity_list')


class UserProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login2')

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request, 'UserProfile.html', {'user': user})


class UserProfileModifyView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login2')

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        form = ModifyProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
        return render(request, 'auth/user_form.html', {'form': form})

    def post(self, request, pk):
        form = ModifyProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=pk)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect(f'/user/profile/{user.pk}')
        else:
            msg = 'Niepoprawne dane'
            return render(request, 'auth/user_form.html', {'form': form, 'msg': msg})


class ChangePasswordView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login2')

    def get(self, request):
        form = ChangePasswordForm
        return render(request, 'auth/user_change_password.html', {'form': form})

    def post(self, request):
        pk = request.POST['pk']
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            u = User.objects.get(pk=pk)
            password = form.cleaned_data['password']
            user = authenticate(username=u.username, password=password)
            if user is not None:
                if form.cleaned_data['new_password'] == form.cleaned_data['check_password']:
                    u.set_password(form.cleaned_data['new_password'])
                    u.save()
                    logout(request)
                    return redirect('login2')
                else:
                    return render(request, 'auth/user_change_password.html', {'form': form, 'msg': 'Hasła nie zgadzają się'})
            else:
                return render(request, 'auth/user_change_password.html', {'form': form, 'msg': 'Błędne hasło'})
        else:
            msg = "Nieprawidłwe dane"
            return render(request, 'auth/user_change_password.html', {'form': form, 'msg': msg})
