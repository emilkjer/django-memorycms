from django.conf.urls import patterns, url

urlpatterns = patterns('api_v1.core_publisher',
    url(r'^$', 'test', name='test'),

    #TODO Remove me
    url(r'entity_base_all$', 'entity_base_all', name='entity_base_all'),

    # API URLS
    url(r'login/$', 'auth_login', name='auth-login'),
    url(r'apps/$', 'apps', name='all-apps'),
    url(r'app/(?P<app_id>\d+)/$', 'get_app_content', name='api-app-show'),
    url(
        r'app/(?P<group_id>\d+)/get_group_content/$',
        'get_group_content',
        name='get-group-content'
    ),
    url(
        r'app/(?P<group_id>\d+)/add_text/$',
        'add_text',
        name='add-text'
    ),
    url(
        r'app/(?P<group_id>\d+)/add_string/$',
        'add_string',
        name='add-string'
    ),
    url(
        r'app/(?P<group_id>\d+)/add_group/$',
        'add_group',
        name='add-group'
    ),
)
