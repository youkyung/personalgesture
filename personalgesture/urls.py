"""personalgesture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'protest.views.index'),
    url(r'^index/$', 'protest.views.index'),
    url(r'^protests/$', 'protest.views.post_list'),
    url(r'^protests/(?P<pk>\d+)/$', 'protest.views.post_detail'),
    url(r'^protests/new/$', 'protest.views.protest_new'),
    url(r'^protests/(?P<pk>\d+)/edit/$', 'protest.views.protest_edit'),
    # url(r'^protests/(?P<protest_pk>\d+)/comments/new/$', 'protest.views.comment_new'),
    # url(r'^protests/(?P<protest_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'protest.views.comment_edit'),
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)