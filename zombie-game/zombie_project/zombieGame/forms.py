from django import forms
from django.contrib.auth.models import User
from zombieGame.models import UserProfile

#Basic user form, creates a username, email and password forms.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#User Profile Form, allows a picture to be uploaded
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
