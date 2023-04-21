from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import NewUserForm

from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this


# Create your views here.

# def register_request(request):
#     return render(request, "register.html", {"register_form": NewUserForm()})


def register_request(request):
    if request.method == "POST":
        print(request.POST)                # backend me data dekhaba ha to
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("in if condition")
            user = form.save()
         #    login(request, user)
            # get request hogi or form show karega
            return redirect("register")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


# from django.contrib.auth.forms import UserCreationForm

# usercreation form ko modif nhi kiya to is case me directly usercreation form ddiya
# US CASE ME username, password, or password confirmation hi hoga

# def register_request(request):
#     return render(request, "register.html", {"register_form": UserCreationForm()})


def login_request(request):    # function based view----user name nikalke authenticate karana hai , data dusre table me insert karna hai 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')    #Archana username 
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)# return user object  # database me comparission karata hai ki apkaa username or password correct hai kya  
            print(user, user.__dict__)
            # if user is not None:
            #     login(request, user)
            #     return redirect("main:homepage")
            if user:
                login(request, user)  # database me save ho jati hi session # login jo session vala table hai vaha pe entry karat hai# or entry karne ke bad konse bhi page pe ja sakte hai
                # return redirect("all_active_books")
                return redirect("home_page")

            else:
                # pass
                return redirect("login_user")    # username or password corrrect nhi hai to eisi page pe regiect karo
        else:
            # pass
            return redirect("login_user")  #form bhi valid nahi to proper data pass nahi kiya to fhir bhi login vale usrer pe ana hai
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


# jab logout karte ho tab jo bhi session me maintain hai o to complete del hoga 
def logout_request(request):               
    logout(request)
    return redirect("login_user")





from django.views.generic import View

from django.contrib.auth import forms


class LoginPageView(View):             # class based view----minor changes
    template_name = 'login.html'       # instance variable 
    form_class = forms.AuthenticationForm

    def get(self, request):
        print("in get method")
        form = self.form_class()
        return render(request, self.template_name, context={'login_form': form})
        
    def post(self, request):
        # print("in post method")
        # print(request.POST)                # username or password milta hai 
        # form = self.form_class(request.POST)
        form = self.form_class(data=request.POST)
        if form.is_valid():
            print(" in valid ")
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'],)
            if user:                     #is not None:
                login(request, user)
                return redirect('home_page')
        message = 'Login failed!'
        return render(request, self.template_name, context={'login_form': form })


# class based view logout



# (b8_env3) C:\Users\DELL\b8_django1\Library2>py manage.py createsuperuser
# Username (leave blank to use 'dell'): Archana
# Email address: archana@gmail.com
# Password: 
# Password (again): python@123
# Superuser created successfully.
