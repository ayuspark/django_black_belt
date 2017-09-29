from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *arg, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user_auth = authenticate(username=username, password=password)
            user_query = User.objects.filter(username=username)
            if not user_query.exists():
                raise forms.ValidationError('User does not exist.')
            if not user_auth:
                raise forms.ValidationError('Somthing is wrong with your username or password.')
            if not user_auth.is_active:
                raise forms.ValidationError('This user is no longer active')
        return super(UserLoginForm, self).clean()


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               min_length=3,
                               help_text='Required. 3 - 150 characters. Letters, digits and @/./+/-/_ only.',
                               max_length=150)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           min_length=8,)
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
                               min_length=8,
                               help_text='At least 8 digits long.')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                       label='Confirm Password',)

    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'password',
            'confirm_password',
        ]
        email = {
            'required': False
        }
    
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        username = self.cleaned_data.get('username')
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match.')
        username_query = User.objects.filter(username__iexact=username)
        if username_query.exists():
            raise forms.ValidationError('Username already exists.')
        return super(UserRegistrationForm, self).clean()
