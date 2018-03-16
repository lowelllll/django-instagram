from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import UserCreationForm # 장고 기본 폼 사용
# def home_sign(request):
#     return render(request, 'registration/home_sign.html')

class Main(CreateView):
    template_name = 'registration/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('auth:login')