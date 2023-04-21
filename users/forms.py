from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2")

    def save(self, commit=True):  # over-ridden save method from Uercreationform
        print("in over-ridden save method")
        # false kiya because email attached karana fhir save karana
        user = super(NewUserForm, self).save(commit=False)
        print(user.__dict__)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['email']
        user.last_name = self.cleaned_data['email']

        if commit:
            user.save()
        return user


# TabError: inconsistent use of tabs and spaces in indentation----code
# copy karne ke bad error

# pip install autopep8

# autopep8 --in-place --aggressive --aggressive "C:\Users\Devidas\Archu_Django08\Library2\users\forms.py"





