from django.conf.urls import patterns, include, url
from blogengine.views import  getPost , getCategory , PostsFeed
from django.views.generic import ListView
from blogengine.views import Category , Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogredef.views.home', name='home'),
    # url(r'^blogredef/', include('blogredef.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Home Page
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
                                               model=Post,
                                               paginate_by=5
                                               )), 
    
    #Blog Posts
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', getPost),
    
    #RSS feeds
    url(r'^feeds/posts/$', PostsFeed()),
    
    # Categories
    url('^categories/?$', ListView.as_view(
                                          model=Category,
                                          )),
    url(r'^categories/(?P<categorySlug>\w+)/?$', getCategory),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d)?$', getCategory),
    
    #Comments
    url(r'^comments/$', include('django.contrib.comments.urls')),
    
    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),

)
