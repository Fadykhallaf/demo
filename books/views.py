from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Book


def index(request):
    books = Book.objects.filter(is_published=True)
    return render(request, 'index.html', {'books': books})


def book_details(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("This book does not exist")
    return render(request, 'book_details.html', {'book': book})
