# -*- coding:UTF-8 -*-
from django import template
from datetime import datetime, timezone
from post.models import Follow
from django.utils.safestring import mark_safe
import re
register = template.Library()

@register.filter
def post_date(upload_date): # date 필터
    now_date = datetime.now(timezone.utc)
    day = now_date - upload_date
    if day.days!=0:
        if day.days > 364 | upload_date.year != now_date.year:
            return "{0}년 {1}월 {2}일".format(upload_date.year,upload_date.month,upload_date.day)
        elif day.days >= 31:
            return "{0}달 전".format(round(day.days/31))
        else:
            return "{0}일 전".format(day.days)
    else:
        if day.seconds//60 < 60:
            return "{0}분 전".format(day.seconds//60)
        else:
            return "{0}시간 전".format(day.seconds//3600)

@register.filter
def tag_link(content,post):
    tags = post.tags.all()
    for tag in tags:
        replace_content = "<a href='/post/tag/{0}'>#{1}</a>".format(tag,tag)
        content= re.sub(r'\#{0}\b'.format(tag),replace_content,content)
    return mark_safe(content)

@register.simple_tag
def is_likes(post,user):
    return post.like_set.filter(user=user,post=post).exists()

@register.simple_tag
def follower_request(user):
    followers = Follow.objects.filter(follower=user.username) # 나를 팔로워 한 사람들
    folloings = Follow.objects.filter(folloing=user.username).values('follower') # 내가 팔로워 한 사람들
    return followers.exclude(folloing__in=folloings).count() # 나를 팔로워 한 사람들 중에 내가 팔로워 한 사람들이면 제외함.
