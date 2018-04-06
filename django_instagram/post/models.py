# -*- coding:UTF-8 -*-
from django.db import models
from django.conf import settings
from django.urls.base import reverse
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/%Y/%m')
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post:post_detail',args=[self.id])

@python_2_unicode_compatible
class Reple(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    author_name = models.CharField(null=True, max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, null=True)  # 생성했을 때

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.content


@python_2_unicode_compatible
class Follow(models.Model):
    folloing = models.CharField(max_length=200)  # 팔로우 한 사람
    follower = models.CharField(max_length=200)  # 팔로우 당한 사람

    def __str__(self):
        return self.folloing

@python_2_unicode_compatible
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
