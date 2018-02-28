from django.conf.urls import url
from .views import *
app_name = 'post'
urlpatterns = [
    url(r'^$',post_list,name='post_list')
]