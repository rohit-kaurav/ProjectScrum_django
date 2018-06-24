from django.conf.urls import url
from project_management.views.project_views import *

urlpatterns = [
    url(r'^$', GetAllProjectsAPI.as_view()),
    url(r'^(?P<project_id>[\s\w\d]+)/$', ProjectAPI.as_view()),
    url(r'^add',ProjectAPI.as_view()),
    url(r'^update', ProjectAPI.as_view()),
]