from django import forms


# class CreateUserForm(forms.Form):
#     username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'nazwa użytkownika'}))
#     password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'haslo'}))
#     password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'powtórz hasło'}))
#
#
# class UserDetailsForm(forms.Form):
#     first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'imię'}))
#     last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'nazwisko'}))
#     email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'email'}))
