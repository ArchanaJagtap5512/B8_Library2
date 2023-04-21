from django import forms
from .models import Book


# creating a form                     # model la use karte ha tab model form 
class BookForm(forms.ModelForm):
    class Meta:
        # only one fields ke liye
        model = Book
        # fields = ("name",)           # comma seperated by default tuple
        fields = "__all__" 
        exclude = ("is_active",)                              # is active ko hatana






# creating a form              # user def to user def form
# class BookForm(forms.Form):
   
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
#     password = forms.CharField(widget = forms.PasswordInput())

#print(BookForm())    # html page create karega 



from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)