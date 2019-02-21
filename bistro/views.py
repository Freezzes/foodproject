from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from .models import Shop,Review,Category
from django.views import generic
import random
import datetime
from django.utils import timezone

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

def result(request):
    keyword = request.GET['shopname']
    bis = Shop.objects.filter(shop_name__startswith =keyword)
    count = len(bis)
    context = { 'lstname':bis,
                'count':count,
                'key':keyword,}
    return  render(request,'bistro/result.html',context)
    
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

def add_review(request):
    
    name = Shop.objects.get(shop_name=request.POST['shopname'])
    score = int(request.POST['likescore'])
    comment = request.POST['message']
    review_date=timezone.now()
    re = Review(name = name,review_date=timezone.now(),score=score,comment=comment )
    re.save()
    userreview = request.POST['user']
    context = { 'name' : userreview,
                'bis':name,
                'score':score,
                'comment':comment,
                'date':review_date}

    return render(request,'bistro/random.html',context)

