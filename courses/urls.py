from django.conf.urls import url
from . import views
from .views import CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, base_name='courses')
urlpatterns = router.urls

# urlpatterns = [
#     url(r'^courses/$', views.CourseList.as_view()),
#     url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view()),
# ]