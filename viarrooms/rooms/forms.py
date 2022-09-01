from django import forms
from .models import Rooms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )


class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['title', 'content', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
    
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Название не должно начитаться с цифры")
        return title
    
class SearchForm(forms.Form):
    date_in = forms.DateField(label='Дата заезда', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_out = forms.DateField(label='Дата выезда', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    peoples = forms.IntegerField(label='Количество человек', widget=forms.TextInput(attrs={'class': 'form-control'}))
    