from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'bloggroup/hometest.html', {})


def about(request):
    return render(request, 'bloggroup/about.html', {})


