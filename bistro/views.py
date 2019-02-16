from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from .models import Shop,review

# Create your views here.
def index(request):
    return render(request,'bistro/index.html')

def search(request):
    context = {
        'bis':Shop.objects.all()
    }
    return render(request, 'bistro/search.html', context)


def find(request):
    return HttpResponse("search from category")

def random(request):
    return HttpResponse("random bistro")

def review_bistro(request):
    return HttpResponse("search from name")