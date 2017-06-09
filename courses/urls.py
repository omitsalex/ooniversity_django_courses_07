from django.conf.urls import url
from . import views


app_name = 'courses'
urlpatterns = [
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<course_id>[0-9]+)/', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<course_id>[0-9]+)/', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<course_id>[0-9]+)/add_lesson$', views.add_lesson, name='add-lesson'),
]