from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.urls.base import reverse
# from django.contrib.auth.models import User
# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True,upload_to='profile/%Y/%m')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post:detail',args=[self.id])

    # 글쓴이
    # 사진
    # 태그->템플릿
    # 태그?
    # 날짜
    # 본문
    # 좋아요
    # oauth
    # 연동