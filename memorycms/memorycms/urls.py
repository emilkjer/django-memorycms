from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'memorycms.views.home', name='home'),
    url(r'', include('core.urls')),

    url(r'^api/register/$', 'auth.views.register'),
    url(r'^api/login/$', 'auth.views.login'),
    url(r'^api/logout/$', 'auth.views.logout'),
    url(r'^api/my_user/$', 'auth.views.my_user'),

    url(r'^api/', include('api_v1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
