
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Форма для обратной связи
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Ваш email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Здесь можно обработать данные (например, отправить на email)
            return HttpResponse('Спасибо за ваше сообщение!')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
