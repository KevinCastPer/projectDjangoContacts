from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Contact
from .forms import ContactForm

def index(request):
    list_contact = Contact.objects.order_by('-nameContact')
    context = {'list_contact' : list_contact}
    return render(request, 'contacts/index.html', context)

def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/detail.html', {'contact': contact})

def formContact(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contacts:index')
    else:
        form = ContactForm()
    return render(request, 'contacts/formContact.html', {'form': form})

def editContact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit = False)
            contact.save()
            return redirect('contacts:index')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/formContact.html', {'form': form})
