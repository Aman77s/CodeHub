from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Count

# Create your views here.

# Home Page Functionality 
def home(request):
    categories = Category.objects.all()
    is_featured = Blogs.objects.filter(is_featured= True).annotate(total_comments=Count('commentmodel'))
    post = Blogs.objects.filter(is_featured=False, choices='published').annotate(total_comments=Count('commentmodel'))
    # Pagination Logic
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'categories': categories, 'is_featured': is_featured, 'page_obj':page_obj })
    
# Categories Page with Post
def category_by_post(request, category_id):
    posts = Blogs.objects.filter(category = category_id).annotate(total_comments=Count('commentmodel'))
    category = get_object_or_404(Category, pk= category_id)
    
    return render(request, 'category.html', {'posts':posts, 'category':category})


# Single Post Functionality
def post(request, slug):
    single_post = get_object_or_404(Blogs, slug = slug )
    recent_posts = Blogs.objects.order_by('-created_at')[:3].annotate(total_comments=Count('commentmodel'))
    author_profile = get_object_or_404(UserProfile, user=single_post.author)
    # Comments 
    if request.method == 'POST':
        comment = CommentModel()
        comment.user = request.user 
        comment.blogs = single_post
        comment.comment = request.POST['textarea']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    
    comments = CommentModel.objects.filter(blogs = single_post)
    comments_count = comments.count()
    context = {
        'single_post': single_post,
        'recent_posts': recent_posts,
        'author_profile': author_profile,
        'comments': comments,
        'comments_count': comments_count
    }
    return render(request, 'single.html', context )


# For Search Functionality
def search(request):
    
    
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(title__icontains = keyword)
    return render(request, 'search.html', {'blogs':blogs, 'keyword':keyword})


def about(request):
    return render(request, 'about.html')