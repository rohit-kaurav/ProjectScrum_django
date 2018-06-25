from django.conf.urls import url

from user_management.views.user_views import *


urlpatterns = [
    url(r'^(?P<employee_id>[\s\w\d]+)/$', User.as_view()),
    url(r'^add$', User.as_view()),
    url(r'^$', GetAllUser.as_view()),
    url(r'^verify/(?P<username>[\s\w\d]+)/$', VerifyUser.as_view()),
    url(r'^authorize$', AuthorizeUser.as_view()),
]
