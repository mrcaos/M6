from django import forms

class LoginForm(forms.form):
    username = forms.CharField(max_length=64,label='Nombre')
    password = forms.PasswordInput(label='Password')
    #email = forms.EmailInput(label='Email')