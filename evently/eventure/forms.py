from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import usersTable

# class SignUpForm(UserCreationForm):

#     class Meta:
#         model = usersTable
#         fields = ("firstName", "lastName", "email", "dateOfBirth")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dateOfBirth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = usersTable
        fields = ["firstName", "lastName", "email", "dateOfBirth", "password1", 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.dateOfBirth = self.cleaned_data['dateOfBirth']
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = usersTable
        fields = ("username", "email")


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)
