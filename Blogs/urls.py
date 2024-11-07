from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Category/<int:category_id>/', views.category_by_post, name= "category_by_post"),
    path('blogs/<slug:slug>', views.post, name='post'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about')
    
] 
