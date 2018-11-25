from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Chronicler


class ChroniclerRegistrationForm(forms.ModelForm):
    emailAddress = forms.EmailField(
        label='이메일',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': Chronicler.email_address,
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': Chronicler.name,
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': Chronicler.password,
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'passwordConfirm',
                'required': 'True',
            }
        )
    )

    class Meta:
        model = Chronicler
        fields = ['email_address', 'name', 'birth_date', 'password']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don`t match")
        return password2

    def save(self, commit=True):
        chronicler = super(ChroniclerRegistrationForm, self).save(commit=False)
        chronicler.set_password(self.cleaned_data['password1'])
        if commit:
            chronicler.save()
        return chronicler


class ChroniclerLoginForm(forms.Form):
    email_address = forms.EmailField(
        label='이메일',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': Chronicler.email_address,
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': Chronicler.password,
                'required': 'True',
            }
        )
    )


class UserChangeForm(forms.ModelForm):

    '''
    password = ReadOnlyPasswordHashField(
        label='Password'
    )
    '''

    class meta:
        model = Chronicler

