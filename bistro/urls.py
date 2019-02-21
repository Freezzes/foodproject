from django.urls import path
from . import views

app_name = 'bistro'
urlpatterns = [
    path('', views.Homepage.as_view(), name='index'),

    path('search/',views.search_name,name='search'),
    path('searchname/',views.result,name='searchname'),

    path('find/', views.Category_View.as_view(), name='find'),
    path('findshop/<int:pk>/',views.Detail_Category.as_view(),name='findshop'),

    path('random/',views.randomshop,name='random'),
    path('review/',views.review_bistro,name='review'),
    path('reviewhere/',views.add_review,name='reviewhere'),

]