from django import forms


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