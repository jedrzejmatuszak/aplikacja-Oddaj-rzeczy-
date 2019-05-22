from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

# from froms import CreateUserForm, UserDetailsForm


class LandingPage(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return HttpResponse()


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('landing_page')
    template_name = 'register.html'




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
