from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = 'post'
urlpatterns = [
    url(r'^$',post_list,name='post_list'),
    url(r'^new/$',Post_create.as_view(),name='post_create'),
]