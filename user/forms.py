from django import forms

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput)
    email = forms.EmailField(label='Email address', required=True)
    first_name = forms.CharField(max_length=120, required=True)
    last_name = forms.CharField(max_length=120, required=True)
    data_of_birth = forms.DateTimeField()
    location = forms.CharField(max_length=120)
    photo = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'location', 'photo')

    def clean(self):
        cd = super().clean()
        email = cd.get('email')
        qs = User.objects.filter(email__iexact=email)
        if cd.get('password') != cd.get('password_2'):
            raise forms.ValidationError("Passwords didn't match. Please try again")
        if qs.exists():
            raise forms.ValidationError("Sorry, this email is already in use.")