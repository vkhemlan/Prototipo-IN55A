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
    (r'^coordinator/(?P<coordinator_id>\d+)/report_description/add$', 'add_report_description'),
    (r'^coordinator/(?P<coordinator_id>\d+)/message$', 'message'),
    (r'^coordinator/(?P<coordinator_id>\d+)/message/(?P<message_ring_id>\d+)$', 'message_details'),
    (r'^coordinator/(?P<coordinator_id>\d+)/message/(?P<message_ring_id>\d+)/reply$', 'message_reply'),
    (r'^coordinator/(?P<coordinator_id>\d+)/message/add$', 'message_add'),
    (r'^coordinator/(?P<coordinator_id>\d+)/indicators$', 'indicators'),
)

urlpatterns += patterns('prototipo.views_group',
    (r'^group/(?P<group_id>\d+)/$', 'index'),
    (r'^group/(?P<group_id>\d+)/report$', 'report'),
    (r'^group/(?P<group_id>\d+)/report/(?P<report_id>\d+)/deliver$', 'deliver_report'),
    (r'^group/(?P<group_id>\d+)/message$', 'message'),
    (r'^group/(?P<group_id>\d+)/message/(?P<message_ring_id>\d+)$', 'message_details'),
    (r'^group/(?P<group_id>\d+)/message/(?P<message_ring_id>\d+)/reply$', 'message_reply'),
    (r'^group/(?P<group_id>\d+)/message/add$', 'message_add'),
)

urlpatterns += patterns('prototipo.views_assistant',
    (r'^assistant/(?P<assistant_id>\d+)$', 'index'),
    (r'^assistant/(?P<assistant_id>\d+)/report$', 'report'),
    (r'^assistant/(?P<assistant_id>\d+)/report/(?P<report_id>\d+)/mark_as_corrected$', 'mark_as_corrected'),
    (r'^assistant/(?P<assistant_id>\d+)/message$', 'message'),
    (r'^assistant/(?P<assistant_id>\d+)/message/(?P<message_ring_id>\d+)$', 'message_details'),
    (r'^assistant/(?P<assistant_id>\d+)/message/(?P<message_ring_id>\d+)/reply$', 'message_reply'),
    (r'^assistant/(?P<assistant_id>\d+)/message/add$', 'message_add'),
)

urlpatterns += patterns('prototipo.views_auxiliary',
    (r'^auxiliary/(?P<auxiliary_id>\d+)$', 'index'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/report$', 'report'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/report/(?P<report_id>\d+)/unmark_as_corrected$', 'unmark_as_corrected'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/report/(?P<report_id>\d+)/mark_as_validated$', 'mark_as_validated'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/message$', 'message'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/message/(?P<message_ring_id>\d+)$', 'message_details'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/message/(?P<message_ring_id>\d+)/reply$', 'message_reply'),
    (r'^auxiliary/(?P<auxiliary_id>\d+)/message/add$', 'message_add'),
)
