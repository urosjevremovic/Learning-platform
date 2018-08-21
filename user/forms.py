from django import forms

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput, required=False)
    email = forms.EmailField(label='Email address', required=True)
    first_name = forms.CharField(max_length=120, required=True)
    last_name = forms.CharField(max_length=120, required=True)
    photo = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'location', 'photo', 'password',
                  'password_2')

    def clean_password_2(self):
        password = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_2')

        if not password_2:
            msg = "You must confirm your password"
            self.add_error('password', msg)
        if password != password_2:
            msg = "Your passwords did not match"
            self.add_error('password', msg)
        return password_2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user