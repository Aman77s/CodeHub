from django.shortcuts import render, redirect, get_object_or_404
from Blogs.models import *
from .forms import * 
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def is_admin_or_editor(user):
    return user.is_staff or user.groups.filter(name='editor').exists()

@user_passes_test(is_admin_or_editor)
def dashboard(request):
    category = Category.objects.all().count()
    post = Blogs.objects.all().count()
    return render (request, 'Dashboard/dashboard.html', {'category': category, 'post': post })

@user_passes_test(is_admin_or_editor)
def category(request):
    return render(request, 'Dashboard/allcategory.html')

@user_passes_test(is_admin_or_editor)
def addcategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
    return render(request, 'Dashboard/addcategory.html', {'form': form})

@user_passes_test(is_admin_or_editor)
def deletecategory(request , pk ):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect ('category')

@user_passes_test(is_admin_or_editor)
def editcategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'Dashboard/editcategory.html', {'form': form, 'category': category})

# Post 

@user_passes_test(is_admin_or_editor)
def allpost(request):
    posts = Blogs.objects.all()
    return render (request, 'Dashboard/allpost.html', {'posts':posts})

@user_passes_test(is_admin_or_editor)
def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('allpost')
        else:
            print(form.errors)
    
    form = PostForm()
    return render(request, 'Dashboard/addpost.html', {'form':form})

@user_passes_test(is_admin_or_editor)
def deletepost(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect('allpost')

@user_passes_test(is_admin_or_editor)
def editpost(request, pk):
    post = get_object_or_404(Blogs, pk=pk )
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('allpost')
        
    else:
        form = PostForm(instance=post)
        
    return render (request, 'Dashboard/editpost.html', {'form': form})

@user_passes_test(is_admin_or_editor)
def UpdateProfile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    return render(request, 'Dashboard/profile.html', {'form': form, 'user_profile': user_profile})
