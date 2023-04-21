from django.shortcuts import HttpResponse, redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Book
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
@csrf_exempt
def home(request):   #  http request
    print(request.method)
    if request.method == "POST":
        # print(request.POST)               # kya data ayaa ya nahi aya 

        #print(request.POST.getlist("cars"))     #get --for single value , getlist--for multiple value

        # bid = request.POST.get("book_id")
        # name = request.POST.get("book_name") # none
        # qty = request.POST.get("book_qty")
        # price = request.POST.get("book_price")
        # author = request.POST.get("book_author")
        # is_pub = request.POST.get("book_is_pub")
        # print(name, qty, price, author, is_pub)
        
        # optimized code

        data = request.POST
        print(data)
        bid = data.get("book_id")
        name = data.get("book_name")
        qty = data.get("book_qty")
        price = data.get("book_price")
        author = data.get("book_author")
        is_pub = data.get("book_is_pub")

        
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False


        if not bid:
            Book.objects.create(name=name, qty=qty, price=price, author=author, is_published=is_pub)
        else:
            book_obj = Book.objects.get(id=bid)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published = is_pub
            book_obj.save()



        #return redirect("home_page")


        #print(request.POST)
        return HttpResponse("Success")
    elif request.method == "GET":
        # print(request.GET) # get query parameter
        # return render(request, "home.html", context={"person_name": "Archana"})
        # return render(request, "home.html", context={"person_names": ["ABC", "XYYZ"]})
        # return render(request, "home.html", context={"all_books": Book.objects.all()})
        return render(request, "old_home.html", context={"person_name": "Archana"})


@login_required
def show_books(request):
    # return render(request, "show_books.html", {"all_books": Book.objects.all()})
    return render(request, "show_books.html", {"books": Book.objects.filter(is_active=True), "active": True})


@login_required
def update_book(request, pk):   # id or pk same
    book_obj = Book.objects.get(id=pk)
    return render(request, "home.html", context={"single_book": book_obj})

@login_required
def delete_book(request, pk):     # hard del---complete database se del hoga 
    Book.objects.get(id=pk).delete()
    return redirect("all_active_books")

@login_required
def soft_delete_book(request, pk):     
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = False
    book_obj.save()
    return redirect("all_inactive_books")

@login_required
def show_inactive_books(request):              # all books lena hai to koi parameter nhi lena only 1 ke lena param
    return render(request, "show_books.html", {"books": Book.objects.filter(is_active=False), "inactive":True})

@login_required
def restore_book(request, id):
    book_obj = Book.objects.get(pk=id)
    book_obj.is_active = True
    book_obj.save()
    return redirect("all_active_books")


# 111

from .forms import BookForm, AddressForm

# def book_form(request):
#     return render(request, "book_form.html", {"form": BookForm()})

@login_required
def book_form(request):
    form = BookForm()
    if request.method == 'POST':
        print(request.POST)
        # name = request.POST.get("name")
        # print(name)
        
        form = BookForm(data=request.POST)
        if form.is_valid():
            # print(form.changed_data.get("name"))           # single data 

            form.save()               # database save
            return HttpResponse("Successfully Registered!!!")
    else:
        context = {'form':form}
        return render(request, "book_form.html", context=context)




# simpleisbetterthancomplex

@login_required
def sibtc(request):
    return render(request, "sibtc.html", {"form": AddressForm()})



# from django.contrib.auth.forms import UserCreationForm  

# def book_form(request):
#     return render(request, "book_form.html", {"form": UserCreationForm()})


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # print("in index function")
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)
    print(page)
    paginator = Paginator(book_list, 3)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    # print(books)
    return render(request, 'index.html', { 'books': books })



# class based view                      # generic view

# from django.views import View  

# class NewView(View):                      # postman ka use karke hit karte hai 
#     def get(self, request):               # get ke alawa getter diya to --this page isn't working 
#         # View logic will place here  
#         return HttpResponse('get response')  

#     def post(self, request):  
#         return HttpResponse('post response')  

#     def put(self, request):               # update
#         return HttpResponse('put response')  

#     def patch(self, request):             # partial info update
#         return HttpResponse('patch response')  

#     def delete(self, request):            # delete
#         return HttpResponse('delete response')  



# 1 create view-----for data creation

# CRUD

from django.views.generic.edit import CreateView  


class BookCreate(CreateView):  # get/post handle 
    model = Book  
    fields = '__all__'  
    # redirect = "BookCreate"           # 302 ---rediect 
    success_url = "/cbv-create-book/"      # or  success_url = reverse_lazy('BookCreate')  



# 2
from django.views.generic.list import ListView  
  
class BookRetrieve(ListView):  
    model = Book
    context_object_name = "all_books"
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']  # get nhi diya to error	   
    # queryset = Book.objects.all()
    # queryset = Book.objects.filter(is_active=1)  # database me se data del karge ga


# override---jo already def tha o abhi work nhi karega # this is overridden method   
# def get_queryset(self):
#     print("in get_queryset method")
    

# def get_queryset(self):
#     print("in method")
#     return Book.objects.filter(is_active=1)   # is_active=0


# detailview


from django.views.generic.detail import DetailView  

class BookDetail(DetailView): 
    model = Book 


# updateview

from django.views.generic.edit import UpdateView  

class BookUpdate(UpdateView):  
    model = Book
    fields = "__all__"
    success_url = "/cbv-create-book/"


# deleteview

from django.views.generic.edit import DeleteView 
  
class BookDelete(DeleteView):  
    model = Book 
  
    # here we can specify the URL   
    # to redirect after successful deletion  
    success_url = "/cbv-create-book/" 




from django.http import HttpResponse
import csv

def create_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'qty', 'price', 'author', 'is_published', 'is_active'])

    books = Book.objects.all().values_list('name', 'qty', 'price', 'author', 'is_published', 'is_active')
    for book in books:
        writer.writerow(book)

    return response



