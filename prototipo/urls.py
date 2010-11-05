from django.conf.urls.defaults import *

urlpatterns = patterns('prototipo.views',
    (r'^login/', 'login'),
    (r'^logout/', 'logout'),
    (r'^coordinator/(?P<coordinator_id>\d+)/$', 'coordinator'),
    (r'^assistant/(?P<assistant_id>\d+)/$', 'assistant'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/$', 'auxiliary'),
    (r'^student/(?P<student_id>\d+)/$', 'student'),
    (r'^$', 'index'),
)

