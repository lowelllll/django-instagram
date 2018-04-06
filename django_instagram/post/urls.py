from django.conf.urls import url
from post.views import *
app_name = 'post'
urlpatterns = [
    url(r'^$',post_list,name='post_list'),
    url(r'^profile/edit/$',profile_update,name='profile_update'),
    url(r'^new/$', Post_create.as_view(), name='post_create'),
    url(r'^modification/(?P<pk>\d+)/$', post_update, name='post_update'),
    url(r'^delete/(?P<pk>\d+)/$', post_delete, name='post_delete'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^(?P<author>\w+)/$',user_post,name='user_post_list'),
    url(r'^(?P<author>\w+)/follow/$', post_follow, name='follow'),
    url(r'^(?P<pk>\d+)/like/$',post_like,name='like'),
    url(r'^search',post_search,name='search'),
    url(r'^tag/(?P<tag>\w+)/$',tag_list,name='tag_list'),
    url(r'^reple/(?P<pk>\d+)/$', post_reple, name="post_reple"),
    url(r'^reples/(?P<pk>\d+)/$', more_reples, name="more_reples")
]