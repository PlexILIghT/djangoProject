from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def homepage_view(request):
    return render(request, 'homepage.html')

def task3(request):
    if request.method == 'GET':
        return render(request, "task3.html", {"request_method": request.method})
    elif request.method == "POST":
        return redirect("redirected", permanent=True)

def redirected(request):
    return HttpResponse(f"<h1>It seems like redirect happened :)</h1>\
                        <h2>Request: {request.method}</h2>")