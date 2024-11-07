from django.urls import path
from . import views 

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Category 
    path('categories/', views.category, name='category' ),
    path('categories/add_categories/', views.addcategory, name='addcategory'),
    path('category/delete<int:pk>', views.deletecategory, name='deletecategory'),
    path('category/edit<int:pk>', views.editcategory, name='editcategory'), 
    
    # Post 
    path('post/', views.allpost, name='allpost'),
    path('post/add/', views.addpost, name='addpost'),
    path('post/delete<int:pk>', views.deletepost, name='deletepost'),
    path('post/edit<int:pk>', views.editpost, name='editpost'), 
    
    
    path('profile/', views.UpdateProfile, name='profile')
    
]

