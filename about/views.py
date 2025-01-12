from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import AboutPage

def about_view(request):
    about_page = AboutPage.objects.first()  # Получаем первую запись
    return render(request, 'about/about.html', {'about_page': about_page})
