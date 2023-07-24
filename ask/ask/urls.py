"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import path, include
    2. Add a URL to urlpatterns:  path(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

from .views import found, not_found, init25
from qa.views import index, popular, ask, login_view, signup

urlpatterns = [

    path('', index),

    path('init25/', init25),
    path('login/', login_view),
    path('signup/', signup),
    path('ask/', ask),
    # path(r'^answer/', answer),
    path('popular/', popular),
    path('new/', found),

    path('admin/', admin.site.urls),
    path('question/', include('qa.urls')),

]
