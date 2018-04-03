from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls.base import reverse_lazy
from django.contrib.auth import get_user_model
from .models import *
from django.conf import settings
from .forms import *
import datetime
from django.http import JsonResponse
from django.db.models import Q
import re

# Create your views here.
@login_required()
def post_list(request):
    posts = Post.objects.select_related('author__profile').prefetch_related('reple_set', 'reple_set__author',
                                                                            'like_set').all()
    return render(request, 'post/post_list.html', {'posts':posts, 'date':datetime.datetime.now()})

@login_required()
def profile_update(request):
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request,'post/profile_form.html',context={'form':form})

class Post_create(CreateView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post:post_list')
    fields = ['content','image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        tags = tag_create(self.request.POST['content'])
        post.tags.add(*tags)  # list 저장하기 위해 * 붙여줌
        post.save()
        return HttpResponseRedirect(self.success_url)

@login_required()
def post_update(request,pk):
    p = get_object_or_404(Post,pk=pk)
    if request.user != p.author:
        return HttpResponse("<script>alert('잘못된 접근입니다.'); history.back();</script>")

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=p)
        if form.is_valid():
            post = form.save()
            return redirect("post:post_detail",post.pk)
    else:
        form = PostForm(instance=p)
    return render(request,"post/post_form.html",{'form':form})

@login_required()
def post_delete(request,pk):
    p = get_object_or_404(Post,pk=pk)
    if request.user!= p.author:
        return HttpResponse("<script>alert('잘못된 접근입니다.'); history.back();</script>")
    p.delete()
    return redirect("post:post_list")

@login_required()
def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    reple_list = Reple.objects.filter(post=pk)
    is_like = Like.objects.filter(post=post,user=request.user).exists()
    like = Like.objects.filter(post=post)
    if request.method == 'POST':
        form = RepleForm(request.POST)
        if form.is_valid():
            reple = Reple(author=request.user,post=post,content=form.cleaned_data['content'])
            reple.save()
            return redirect(post)
    else:
        form = RepleForm()
        context = {
            'post': post,
            'form': form,
            'reple_list': reple_list,
            'is_like': is_like,
            'like': like
        }
    return render(request,'post/post_detail.html',context)

@login_required()
def user_post(request,author):
    User = get_user_model()
    user = User.objects.get(username=author)
    folloing = Follow.objects.filter(folloing=author).count()
    follower = Follow.objects.filter(follower=author).count()
    posts = Post.objects.filter(author=user)
    is_follow = Follow.objects.filter(follower=author,folloing=request.user).exists() # 해당 객체가 있으면 True,없으면 False 리턴
    context = {
        'posts':posts,
        'author':user,
        'is_follow':is_follow,
        'folloing':folloing,
        'follower':follower
    }
    return render(request,'post/user_post_list.html',context)


@login_required()
def post_follow(request, author):
    follow, flag = Follow.objects.get_or_create(follower=author, folloing=request.user)
    if not flag:  # 원래 객체가 존재했다면
        follow.delete()
        message = "팔로잉"
    else:
        message = "팔로우"

    follow_count = Follow.objects.filter(follower=author).count()
    data = {
        'follow_count': follow_count,
        'message': message
    }
    return JsonResponse(data)


@login_required()
def post_like(request,pk):
    post = Post.objects.get(pk=pk)
    like,flag = Like.objects.get_or_create(post=post,user=request.user)
    if not flag:
        like.delete()
        message = 'like'
    else:
        message = 'liked'
    like_count = Like.objects.filter(post=post).count()
    data = {
        'message':message,
        'like_count':like_count
    }
    return JsonResponse(data)

@login_required()
def post_search(request):
    word  = request.GET.get('word', None)
    User = get_user_model()
    try:
        users = User.objects.filter(
            Q(username__icontains=word) | Q(email__icontains=word)
        ).values()
        profiles = Profile.objects.filter(
            Q(user__username__icontains=word) | Q(user__email__icontains=word)
        ).values()
        data = {
            'flag':True,
            'profile':list(profiles),
            'data': list(users)
        }
        return JsonResponse(data)
    except:
        return JsonResponse({
            'flag':False
        })

@login_required()
def tag_list(request,tag):
    t = Tag.objects.get(tag=tag)
    posts = t.post_set.all()
    return render(request,'post/tag_list.html',{'posts':posts})

def tag_create(content):
    find_tags = "".join(re.findall('#\w{0,20}\s', content))
    find_tags = re.sub("\s", "", find_tags)
    temp_tags = re.split("#", find_tags)
    tags = []
    for temp_tag in temp_tags:
        if temp_tag == '':
            continue
        else:
            tag, flag = Tag.objects.get_or_create(tag=temp_tag)
            tags.append(tag)
    return tags

@login_required()
def post_reple(request,pk):
    try:
        post = Post.objects.get(pk=pk)
        comment = request.GET.get('comment')
        reple = Reple(author = request.user , post=post,content=comment)
        reple.save()
        data = {
            'reple':reple.content,
            'author':reple.author.username,
            'flag':True
        }
        return JsonResponse(data)
    except:
        data = {
            'flag':False
        }
        return JsonResponse(data)