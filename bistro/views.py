from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from .models import Shop,review
from django.views import generic
import random

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'bistro/find.html'
    context_object_name = 'latest_shop_list'

    def get_queryset(self):
        return Shop.objects.order_by('category')

class DetialView(generic.ListView):
    template_name = 'bistro/index.html'
    context_object_name = 'latest_shop_list'

    def get_queryset(self):
        return Shop.objects.order_by('shop_name')

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

def randomshop(request):
    shops = Shop.objects.all()
    random_shop = Shop.objects.all(random=Shop.shop_name)
    cont = {'rs':random_shop}
    return render(request,'bistro/random.html')

def review_bistro(request):
    return render(request,'bistro/review.html')

