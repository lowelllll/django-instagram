from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post,Reple
from .forms import PostForm,RepleForm
import datetime
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls.base import reverse_lazy
# Create your views here.

@login_required()
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts':posts, 'date':datetime.datetime.now()})

# @login_required()
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             p = Post(author=request.user,content=form.cleaned_data['content'],image=form.cleaned_data['image'],date=datetime.timezone.now())
#             p.save()
#             return HttpResponseRedirect('post:post_list')
#     else:
#         form = PostForm()
#
#     return render(request,'post/post_form.html',{'form':form})
@login_required()
def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    reple_list = Reple.objects.filter(post=pk)
    if request.method == 'POST':
        form = RepleForm(request.POST)
        if form.is_valid():
            reple = Reple(author=request.user,post=post,content=form.cleaned_data['content'])
            reple.save()
            return HttpResponseRedirect(reverse_lazy('post:post_detail',args=pk))
    else:
        form = RepleForm()
    return render(request,'post/post_detail.html',{'post':post,'form':form,'reple_list':reple_list})

class Post_create(CreateView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post:post_list')
    fields = ['content','image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Post_create,self).form_valid(form)

class Post_update(UpdateView,LoginRequiredMixin):
    model = Post
    fields = ['content','image']
    success_url = reverse_lazy('post:post_list')

class Post_delete(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post:post_list')


