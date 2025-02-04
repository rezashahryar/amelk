from django import forms
from django.core.validators import validate_integer, validate_email

from accounts.models import User


class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=11, validators=[validate_integer])
    password = forms.CharField()


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['mobile', 'email']

    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data['mobile']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user
