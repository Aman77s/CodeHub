from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name
        
STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published')
)
        
class Blogs(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    blog_image = models.ImageField(upload_to='upload')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_body = RichTextField()
    choices = models.CharField(max_length=100,  choices = STATUS_CHOICE, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
        
    class Meta:
        verbose_name_plural = 'Blogs'
        
    def __str__(self):
        return self.title
    
# User Profile Model 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.comment
    

    
    
    

