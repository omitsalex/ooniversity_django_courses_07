"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.urls import include, path
from quadratic.views import quadratic_results
from . import views

urlpatterns = [
#    path('', views.index, name='index'),
#    path('polls/', include('polls.urls')),
#    path('admin/', admin.site.urls),
#    path('contact/', views.contact, name='contact'),
#    path('student_list/', views.student_list, name='student_list'),
#    path('student_detail/', views.student_detail, name='student_detail'),
    url(r'^$', views.index, name='index'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls')),
]
