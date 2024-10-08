"""travelia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from travelia import settings
from django.urls import path, include
## Core URLs
from core import urls
## Places URLs
from places import urls
## Work URLs
from work import urls
## Article URLs
from article import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    # Places URLs
    path("", include("places.urls")),
    # Work URLs
    path("", include("work.urls")),
    ## Article URLs
    path("", include("article.urls")),
]

#! MEDIA
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)