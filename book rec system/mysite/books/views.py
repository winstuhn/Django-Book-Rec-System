from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import *
from .forms import BookForm
from .book_rec import search_book



def index(request):
    return HttpResponse("Hello, world. You're at the book index.")

def get_book(request):
    print(request.method)
    list_of_books = []
    if request.method == 'POST':
        try:
            book = request.POST.get('textfield', None)
            print(book)
            book_rec = search_book(str(book))
            for data in book_rec:
                list_of_books.append(data)
            return render (request, "page.html",{"books":list_of_books})
        except:
            context ={}
            context['form']= BookForm()
            return render(request, "home.html", context)
        
    else:
        context ={}
        context['form']= BookForm()
        return render(request, "home.html", context)