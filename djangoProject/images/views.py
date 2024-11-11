from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Image
from django.conf import settings
# Create your views here.

def show_image(request):
    images = Image.objects.all()
    return render(request, "image_task2.html", {'images': images, "request_method": request.method})
