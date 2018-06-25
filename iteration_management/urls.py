from django.conf.urls import url
from iteration_management.views.iteration_views import *

urlpatterns = [
    url(r'^$', GetAllIterationsAPI.as_view()),
    url(r'^(?P<iteration_name>[\s\w\d]+)/$', IterationAPI.as_view()),
    url(r'^add',IterationAPI.as_view()),
    url(r'^update', IterationAPI.as_view()),
]