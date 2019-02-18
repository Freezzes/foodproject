from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from .models import Shop,Review,Category
from django.views import generic
import random

# Create your views here.
class Category_View(generic.ListView):
    template_name = 'bistro/find.html'
    context_object_name = 'latest_category_list'

    def get_queryset(self):
        return Category.objects.order_by('category_name')

class Detail_Category(generic.DetailView):
    model = Category
    template_name = 'bistro/showtype.html'

class Homepage(generic.ListView):
    template_name = 'bistro/index.html'
    context_object_name = 'latest_shop_list'

    def get_queryset(self):
        return Shop.objects.order_by('shop_name')

def search_name(request):
    return render(request,'bistro/search.html')

def showexplanation(request):
    try:
        search_bis = Shop.objects.get(shop_name=request.GET['restname'])
    except (KeyError, Shop.DoesNotExist):
        return render(request, 'bistro/search.html', {
            'error_message': "Not found.",
        })    
    context = {
        'bis':search_bis.shop_name,
        'explain': search_bis.explanation,
    }
    return render(request, 'bistro/show.html', context)


def randomshop(request):
    shops = Shop.objects.all()
    random_shop = Shop.objects.all(random=Shop.shop_name)
    cont = {'rs':random_shop}
    return render(request,'bistro/random.html')

def review_bistro(request):
    return render(request,'bistro/review.html')

