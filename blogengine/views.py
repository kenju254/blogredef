# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from blogengine.models import Post, Category
from django.template import RequestContext
from django.contrib.syndication.views import Feed


def getPosts(request, selected_page=1):
    # Get all blog posts
    posts = Post.objects.all().order_by('-pub_date')
    
    #Adding Pagination to the blogengine
    pages = Paginator(posts, 5)
    
    #Getting the Specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    
    #Display all the posts
    return render_to_response('posts.html', {'posts':returned_page.object_list, 'page':returned_page})

def getPost(request, postSlug):    
    #Get Specific Post
    post = Post.objects.filter(slug=postSlug)
    
    #Display specific post
    return render_to_response('single.html',{'posts': post}, context_instance=RequestContext(request))

def getCategory(request, categorySlug, selected_page=1):
    # Get specified category
    posts = Post.objects.all().order_by('-pub_date')
    category_posts = []
    for post in posts:
        if post.categories.filter(slug=categorySlug):
            category_posts.append(post)
            
    # Pagination
    pages = Paginator(category_posts, 5)
    
    #Get the category
    category = Category.objects.filter(slug=categorySlug)[0]
    
    #Get Specific Page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    
    #Display all the posts
    return render_to_response('category.html', {'posts':returned_page.object_list,'page':returned_page, 'category':category})
        
class PostsFeed(Feed):
    title = "Kenju254 Chronicles posts"
    link = "feeds/posts/"
    description = "Posts from Kenju254 Chronicles"
    
    def item(self):
        return Post.objects.order_by('-pub_date')[:5]
    
    
    
    
         
