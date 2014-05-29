from django.conf.urls import patterns, url, include
from .views import PartialGroupView



partial_patterns = patterns('',
    #TODO this can be done in a smarter way...
    url(
        r'^app-all.html$',
        PartialGroupView.as_view(template_name='app-all.html'),
        name='app_all'
    ),
    url(
        r'^app-detail.html$',
        PartialGroupView.as_view(template_name='app-detail.html'),
        name='app_detail'
    ),
)


urlpatterns = patterns('core.views',

    url(r'^$', 'apps_show', name='apps-show'),

    url(r'^partials/', include(partial_patterns, namespace='partials')),


    # ADD
    url(r'^tools/app_add/$',
        'app_add', name='app-add'),

    url(r'^tools/(?P<group_id>\w+)/entity_add_text/$',
        'entity_add_text', name='entity-add-text'),
    url(r'^tools/(?P<group_id>\w+)/entity_add_string/$',
        'entity_add_string', name='entity-add-string'),
    url(r'^tools/(?P<group_id>\w+)/entity_add_group/$',
        'entity_add_group', name='entity-add-group'),


    # SHOW
    url(r'^show/(?P<group_id>\w+)/entity_show_group/$',
        'entity_show_group', name='entity-show-group'),

    url(r'^app/(?P<app_id>\w+)/$', 'app_show', name='app-show'),
    
    # url(r'^app/(?P<app_id>\w+)/$', 'group_add', name='group-add'),
)
