from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'd51.django.apps.email_capture.views',
    url(r'store/$', 'store', name='email_capture_store'),
)
