from django.shortcuts import render

# Create your views here.


def view_contact(request):

    return render(request, "contact/contact.html")
