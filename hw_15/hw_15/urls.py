"""hw_15 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
from currency.views import index, currency
from lecture.views import lecture
from contacts.views import contacts
from passport.views import passport

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^currency', currency, name='currency'),
    url(r'^lecture', lecture, name='lecture'),
    url(r'^passport', passport, name='passport'),
    url(r'^contacts', contacts, name='contacts'),
]
