from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', max_length=20)
    email = forms.EmailField(label='email', max_length=50)
