# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from blogengine.models import Post


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
    return render_to_response('posts.html',{'posts': post})

