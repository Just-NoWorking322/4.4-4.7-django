
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})
