from django.contrib import admin
from .models import Category, Blogs, UserProfile, CommentModel

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_featured')
    prepopulated_fields = {'slug':('title', )}
    search_fields = ('id', 'title')
    list_editable = ('is_featured' , )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(UserProfile)
admin.site.register(CommentModel)
