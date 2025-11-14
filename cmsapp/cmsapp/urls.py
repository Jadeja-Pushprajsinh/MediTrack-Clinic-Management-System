"""
URL configuration for cmsapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from doctor.views import *
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',show_register),
    path('',show_login),
    path('login',login,name='login'),
    path('dashboard',show_dashboard,name='show_dashboard'),
    path('patients/add',show_add_patient,name='show_add_patient')
]
