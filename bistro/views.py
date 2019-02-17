from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from .models import Shop,review

# Create your views here.
def index(request):
    return render(request,'bistro/index.html')

def search(request):
    return render(request,'bistro/search.html')

def showsearch(request):
    bis = Shop.objects.all()
    search_bis = Shop.objects.get(shop_name=request.POST['restname'])
    context = {
        'bis': search_bis,
    }
    return render(request, 'bistro/show.html', context)


def find(request):
    return render(request,'bistro/find.html')

def random(request):
    return HttpResponse("random bistro")

def review_bistro(request):
    return HttpResponse("search from name")