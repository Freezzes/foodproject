from django.urls import path
from . import views

app_name = 'bistro'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/',views.search,name='search'),
    path('searchname/',views.showsearch,name='searchname'),
    path('find/',views.find,name='find'),
    path('random/',views.random,name='random'),
    path('review/',views.review_bistro,name='review'),

]