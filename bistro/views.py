from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'bistro/index.html')

def search(request):
    return HttpResponse("search from name")

def find(request):
    return HttpResponse("search from category")

def random(request):
    return HttpResponse("random bistro")

def review_bistro(request):
    return HttpResponse("search from name")