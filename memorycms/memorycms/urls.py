from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'memorycms.views.home', name='home'),
    url(r'', include('core.urls')),

    url(r'^api/', include('api_v1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
