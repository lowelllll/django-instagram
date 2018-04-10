"""django_instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/',include('post.urls',namespace='post')),
    url(r'^accounts/',include('django.contrib.auth.urls',namespace='account')),
    # django/contrib/auth/urls.py app_name ='account'
    # Reverse for 'password_change_done' not found. 'password_change_done' is not a valid view function or pattern name.
    # solve : path('password_change/', views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    url(r'^$',Main.as_view(),name='main'),
    url(r'',include('social_django.urls',namespace='social'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
