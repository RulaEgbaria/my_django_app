"""my_django_app URL Configuration

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
from django.urls import path

from hello import views
# from hello.views import index
# from hello.views import login_user
# from hello.views import visitor
# from hello.views import sign_in
# from hello.views import sign_up
# from hello.views import questionnaire


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('visitor/', views.visitor, name='visitor'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('login_user/sign_in/', views.sign_in, name='sign_in'),
    path('login_user/sign_up/', views.sign_up, name='sign_up'),




]
