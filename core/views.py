from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, ListView
from forms import LoginForm, SignUpForm


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
            User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
            return redirect('landing_page')
        else:
            msg = 'Hasła są niezgodne'
            return render(self.request, 'register.html', {'form': form, 'msg': msg})

class AdminListView(View):

    def get(self, request):
        admins = User.objects.filter(groups__name='Administrator')
        su = User.objects.filter(is_superuser=True)
        return render(request, 'adminList.html', {'admins': admins, 'su': su})



# class SignUpView(FormView):
#
#     template_name = 'register.html'
#     form_class = CreateUserForm
#     # success_url = reverse_lazy('user-details')
#
#     def form_valid(self, form):
#         if form.cleaned_data['password1'] != form.cleaned_data['password2']:
#             return render(self.request, 'register.html', {'msg': 'Hasła się nie zgadzaja', 'form': form})
#         user = User.objects.create(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password1']
#         )
#         return redirect(f'signup/details/{user.id}')
#
#     def form_invalid(self, form):
#         return render(self.request, 'register.html', {'msg': 'Niepoprawne dane', 'form': form})


# class UserDetails(View):
#
#     def get(self, request, pk):
#         form = UserDetailsForm
#         return render(request, 'addDetails.html', {'form': form})
#
#     def post(self, request, pk):
#         form = UserDetailsForm(request.POST)
#         user = User.objects.get(id=pk)
#         if form.is_valid():
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.email = form.cleaned_data['email']
#             user.save()
#         return redirect('/')
