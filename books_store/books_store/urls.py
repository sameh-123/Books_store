"""
URL configuration for books_store project.

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
from django.contrib import admin
from django.urls import path
from home.views import *
from student.views import *
from employee.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home',home),
    path('signin',signin),
    path('signup',signup),
    path('student_page',student_page,name='student_page'),
    path('add_book',add_book),
    path('borrow_book',borrow_book),
    path('loginadmin',loginadmin),
    path('admin-page',admin_page),
    path('changeadminpass',changeadminpass),
<<<<<<< HEAD
    path('update',update),
=======
    path('logout',logout),
    path('all_users',allusers),
    path('all_books',allbooks),
    path('deletebook/<int:id>',deletebook,name='deletebook'),
    path('addbook',addbook,name='addbook'),
>>>>>>> 9cfbf1d7c0403feab2509b13aca9d6782e49bc16
    
]
