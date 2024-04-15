"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mblog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('about/', views.about, name= 'about'),

    path('contact/', views.contact, name='contact'),


    path('userinfo/add/', views.info_view, name='info'),
    path('userinfo/add/', views.info_view, name='infos'),

    path('', include('mblog.urls')),

    path('post/<slug:slug>/', views.post_detail, name='post_detail'),

    path('like_post/', views.like_post, name='like_post'),


]
if settings.DEBUG :
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)