from django import forms
from django.contrib.auth.models import User, Group
from django.forms import ModelForm

from .models import Charity, HELP


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email'}))
    password = forms.CharField(
        label="Hasło",
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        label='Nazwa użytkownika',
        widget=forms.TextInput(
            attrs={'placeholder': 'Nazwa użytkownika'}
        )
    )
    first_name = forms.CharField(
        label='Imię',
        widget=forms.TextInput(
            attrs={'placeholder': 'Imię'}
        )
    )
    last_name = forms.CharField(
        label='Nazwisko',
        widget=forms.TextInput(
            attrs={'placeholder': 'Nazwisko'}
        )
    )
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email'}
        )
    )
    password1 = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Hasło'}
        )
    )
    password2 = forms.CharField(
        label='Powtórz hasło',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Powtórz hasło'}
        )
    )


class SetAdminPermissionForm(forms.Form):
    user = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(groups__name='Użytkownik'),
        label='Użytkownik',
    )


class AddAdminForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UpdateCharityForm(ModelForm):

    class Meta:
        model = Charity
        fields = '__all__'

    help = forms.CharField(
        label='Komu niesie pomoc',
        required=True,
        widget=forms.CheckboxSelectMultiple(
            choices=HELP
        )
    )
