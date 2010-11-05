from django.conf.urls.defaults import *

urlpatterns = patterns('prototipo.views',
    (r'^login/', 'login'),
    (r'^logout/', 'logout'),
    (r'^$', 'index'),
)

