from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def history(request):
    return HttpResponse("<h4>History is repeating AAAAAA!!!!!!!<h4>")
