from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
import datetime
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls.base import reverse_lazy
# Create your views here.

@login_required()
def post_list(request):
    posts = Post.objects.all()
    return render(request,'post/post-list.html',{'posts':posts})

@login_required()
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(author=request.user,content=form.cleaned_data['content'],image=form.cleaned_data['image'],date=datetime.timezone.now())
            p.save()
            return HttpResponseRedirect('post:post_list')
    else:
        form = PostForm()

    return render(request,'post/post_form.html',{'form':form})

class Post_create(CreateView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post:post_list')
    fields = ['content','image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Post_create,self).form_valid(form)
    # 이미지 깨짐 왜?


