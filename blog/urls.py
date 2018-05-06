from django.conf.urls import url #to map out our urls

from .views import PostListView, PostDetailView, post_detail, post_list#functions from views
#http://example.com/blog/
urlpatterns = [
    url(r'^blog-list/$', PostListView.as_view(), name='blog_list_view'),#http://example.com/blog/blog-list-function/
    #url(r'^blog-detail/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='blog_detail_view'),#class based detailview= PostDetailView.as_view()
    url(r'^blog-list-function/$', post_list, name="post_list"),##http://example.com/blog/blog-list-function/ function based view = post_list
    url(r'^blog-detail/(?P<slug>[-\w]+)/$', post_detail, name="blog_detail"),#function based detail view,
]
