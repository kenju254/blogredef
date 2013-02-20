from django.conf.urls import patterns, include, url
from blogengine.views import getPosts, getPost

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
    url(r'^$' ,getPosts),
    url(r'^(?P<selected_page>\d+)/?$', 'blogengine.views.getPosts'),
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', getPost),
    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),

)
