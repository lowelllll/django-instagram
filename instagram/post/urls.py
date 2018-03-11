from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = 'post'
urlpatterns = [
    url(r'^$',post_list,name='post_list'),
    url(r'^new/$',Post_create.as_view(),name='post_create'),
    url(r'^modification/(?P<pk>\d+)/$',Post_update.as_view(),name='post_update'),
    url(r'^(?P<pk>\d+)/$',post_detail,name='post_detail'),
    url(r'^(?P<author>\w+)/$',user_post,name='user_post_list'),
    url(r'^(?P<author>\w+)/follow/$',post_follow,name='follow'),
]