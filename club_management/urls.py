"""
URL configuration for club_management project.

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
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # api routs
    path('api/kunden/', include('kunden.urls')),
    path('api/kalender/', include('kalender.urls')),

    # app sites
    path('kunden/', include('kunden.urls')),
    path('auftraege/', include('auftraege.urls')),
    path('kalender/', include('kalender.urls')),
    path('workshops/', include('workshops.urls')),

    # login
    path('accounts/', include('django.contrib.auth.urls')),  # added for login and logout


    
]
