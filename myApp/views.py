from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1 style='color:red;'>our webpage</h1>")
