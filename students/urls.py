from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
]