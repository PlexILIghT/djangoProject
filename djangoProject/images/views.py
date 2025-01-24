from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Image
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_image(request):
    images = Image.objects.all()
    for image in images:
        image.is_liked = request.user in image.liked_by.all() if request.user.is_authenticated else False
    return render(request, "images.html", {'images': images})

@login_required
def like_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.user in image.liked_by.all():
        image.liked_by.remove(request.user)
    else:
        image.liked_by.add(request.user)

    return redirect('show_images')  # Перенаправление обратно на страницу с изображениями
