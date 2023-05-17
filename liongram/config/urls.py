"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from demos.views import lotto, lotto_result
from posts.views import index, url_view, url_parameter_view, function_view, class_view, function_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', lotto, name="lotto"),
    path('lotto/result/', lotto_result, name='lotto_result'),
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    path('fbv/list', function_list_view),
    path('cbv/', class_view.as_view()),

    path('', index, name="index"),
    path('posts/', include('posts.urls', namespace = 'posts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
