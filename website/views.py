from curses.ascii import HT
from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message submitted successfully')
        else:
            messages.error(request, "Your message did't submitted")
    else:
        form = ContactForm()
    return render(request, 'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')