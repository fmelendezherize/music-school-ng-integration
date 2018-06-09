"""musicschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

schema_view = get_swagger_view(title='Music School API')

#url(r'^$', schema_view),

urlpatterns = [
    url(r'^$', serve,kwargs={'path': 'index.html'}),
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
    RedirectView.as_view(url='/static/%(path)s', permanent=False)),
    url(r'^schema/', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('courses.urls')),
    url(r'^api/', include('professors.urls')),
    url(r'^api/', include('students.urls')),
]
