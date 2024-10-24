"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from management.views import post_list,post_details,index,user_login,user_logout,admin_panel

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('posts/',post_list,name='blog'),
    path('posts/<int:post_id>',post_details,name='post_details'),
    path('',index,name='home'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('admin-panel/',admin_panel,name='admin_panel')
]
