from django.urls import path
from . import views

app_name = 'bistro'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    path('search/',views.search,name='search'),
    path('searchname/',views.showsearch,name='searchname'),

    path('find/', views.IndexView.as_view(), name='find'),
    path('findshop/<int:pk>/',views.DetailView.as_view(),name='findshop'),

    path('random/',views.randomshop,name='random'),
    path('review/',views.review_bistro,name='review'),

]