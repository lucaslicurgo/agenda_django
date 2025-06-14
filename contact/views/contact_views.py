from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all().order_by('-id')
    context = {
        'contacts': contacts
    }

    return render(
        request,
        'contact/index.html',
        context
    )