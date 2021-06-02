from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class Login_Form(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class Registration(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Повтори пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_repeatPassword(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['repeat_password']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message_txt']
        labels = {'message_txt': ""}
