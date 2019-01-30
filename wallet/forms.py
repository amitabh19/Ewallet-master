from django.contrib.auth.forms import UserCreationForm, forms
from .models import User, UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['mob', ]