from django.forms import ModelForm
from .models import Car#, Review, EnginesPlts, Options
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'content']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class ReviewForm(ModelForm):
#     class Meta:
#         model = Review
#         fields = ['content']
#
# class EnginesPltsForm(ModelForm):
#     class Meta:
#         model = EnginesPlts
#         fields = ['content']
#
# class OptionsForm(ModelForm):
#     class Meta:
#         model = Options
#         fields = ['content']