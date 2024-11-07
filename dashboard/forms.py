from django import forms
from Blogs.models import *

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        
        
class PostForm(forms.ModelForm):
    
    
    class Meta:
        model = Blogs
        fields = ('title','blog_image', 'category', 'blog_body', 'choices', 'is_featured')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture']
        
    