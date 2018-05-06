"""example URL Configuration

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
from django.conf.urls import url, include #include function
from django.contrib import admin

from .views import home #This is how we connect our view home(views.py) to our urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),#when a user visits http://127.0.0.1:8000/, name='home' can be used in templates
    url(r'^blog/', include('blog.urls', app_name='blog', namespace='blog')),#http://example.com/blog/
]
