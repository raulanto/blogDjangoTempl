from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from ..models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'input input-bordered w-full max-w-xs',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'input input-bordered w-full max-w-xs',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'input input-bordered w-full max-w-xs'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'file-input w-full'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'input input-bordered w-full ', 'rows': 5}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered w-full ', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio','ciudad']
