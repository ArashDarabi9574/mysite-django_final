from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.forms import ContactForm, NewsLetterForm
from django.contrib import messages

def index_view(response):
    return render(response, 'website/index.html')


def about_view(response):
    return render(response, 'website/about.html')


def newsletter_view(response):
    if response.method == 'POST':
        form = NewsLetterForm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def contact_view(response):
    if response.method == 'POST':
        form = ContactForm(response.POST)
        if form.is_valid():
            fs= form.save(commit=False)
            fs.name= "uknown"
            fs.save()
            messages.add_message(response, messages.SUCCESS,'successfully!')
        else:
            messages.add_message(response, messages.ERROR,'your ticket didnt submited!')
    form = ContactForm()
    return render(response, 'website/contact.html')

def handler_not_found(request, exception):
    return render(request, 'not-found.html')