from django.shortcuts import render, redirect

from books.models import Book

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    page_date = request.GET.get("date")
    if page_date == None:
        books = Book.objects.all()
        context = {'books': books}
    else:
        books = Book.objects.filter(pub_date=page_date)
        forward_page = Book.objects.filter(pub_date__gt=page_date).order_by('pub_date')
        if list(forward_page) == []:
            forward_page = [None]
        back_page = Book.objects.filter(pub_date__lt=page_date).order_by('-pub_date')
        if list(back_page) == []:
            back_page = [None]


        context = {'books': books,
                   'text_pages': '| другая дата |',
                   'forward': forward_page[0],
                   'back': back_page[0],
                   }

    return render(request, template, context)
