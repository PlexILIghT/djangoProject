from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("")

def show_image(request):
    return render(request, "image.html")