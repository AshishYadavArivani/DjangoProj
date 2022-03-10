"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from mysite import views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls'))
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('id/<int:id>', views.get_data),
    path('string/<str:id>', views.get_data),
    path('id/<int:id>', views.get_data),
    path('slug/<slug:id>', views.get_data),
    path('all/<id>', views.get_data),
    path('save_data/', views.save_data),
    path('delete/<id>', views.delete_detail),
    path('edit/<id>', views.edit_detail),
    path('edit/update_data/<id>', views.update_detail,name='update'),
    path('register/', views.register,name='register'),
    path('store_register/', views.store_register,name='store_register'),
    path('login/', views.login),
    path('login_store/', views.login_store),
    path('logout/', views.logout),

    path('session_set/', views.session_set),
    path('session_get/', views.session_get),
    path('session_delete/', views.session_delete),
]
handler404 = views.bad_request