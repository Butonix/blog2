from django.conf.urls import url #to map out our urls

from .views import  post_detail, post_list, category_detail, search, new_post, post_list_admin, edit_post, delete_post#functions from views
#http://example.com/blog/
urlpatterns = [
    url(r'^blog-list/$', post_list, name="post_list"),##http://example.com/blog/blog-list-function/ function based view = post_list
    url(r'^results/$', search, name="search"),
    url(r'^blog-detail/(?P<slug>[-\w]+)/$', post_detail, name="blog_detail"),#function based detail view,
    url(r'^category-detail/(?P<slug>[-\w]+)/$', category_detail, name="category_detail"),#function based category_detail view
    url(r'^new-post/$', new_post, name='new_post'),
    url(r'^post-list/$', post_list_admin, name='post_list_admin'),
    url(r'^edit-post/(?P<pk>\d+)/$', edit_post, name='edit_post'),
    url(r'^delete-post/(?P<pk>\d+)/$', delete_post, name='delete_post'),
]
