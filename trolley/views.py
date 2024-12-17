from django.shortcuts import render

# Create your views here.


def show_trolley(request):

    return render(request, "trolley/trolley.html")
