from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={ "placeholder": "Username", "class": "form-control"})),
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"})),


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email","class": "form-control"}))
    hemis_id = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Hemis ID","class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password check","class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'hemis_id', 'password1', 'password2')


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg


class ArizaForm(forms.Form):
    foydalanuvchi_id = forms.IntegerField(widget=forms.HiddenInput()),
    admin_turi = forms.ChoiceField(choices=[('hemis', 'Hemis_admin'), ('moodle', 'Moodle_admin'), ('kerocontrol', 'KeroControl_admin')]),
    malumotlar = forms.CharField(widget=forms.Textarea),


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']