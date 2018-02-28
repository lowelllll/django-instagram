from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def post_list(request):
    return render(request,'post/post-list.html')