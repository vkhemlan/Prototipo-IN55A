from django.conf.urls.defaults import *

urlpatterns = patterns('prototipo.views',
    (r'^login/', 'login'),
    (r'^logout/', 'logout'),
    (r'^assistant/(?P<assistant_id>\d+)/$', 'assistant'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/$', 'auxiliary'),
    (r'^student/(?P<student_id>\d+)/$', 'student'),
    (r'^$', 'index'),
)

urlpatterns += patterns('prototipo.views_coordinator',
    (r'^coordinator/(?P<coordinator_id>\d+)/$', 'index'),
    (r'^coordinator/(?P<coordinator_id>\d+)/report_description$', 'report_description'),
    (r'^coordinator/(?P<coordinator_id>\d+)/report_description/add$', 'add_report_description')
) 
